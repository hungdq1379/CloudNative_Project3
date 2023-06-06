import logging
import random
import time

from flask_pymongo import PyMongo
from flask import Flask, request, jsonify
from flask_opentracing import FlaskTracing
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Summary, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Create a metric to track time spent and requests made.
s = Summary('request_processing_seconds', 'Time spent processing request')
c = Counter('my_failures', 'Description of counter')

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

metrics = PrometheusMetrics(app)
# static information as metric
metrics.info("app_info", "Application info", version="1.0.3")

logging.getLogger("").handlers = []
logging.basicConfig(format="%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# register additional default metrics
metrics.register_default(
    metrics.counter(
        'request_by_path_counter', 'Request count by request path',
        labels={'path': lambda: request.path}
    )
)

def init_tracer(service):

    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "reporter_batch_size": 1,
        },
        service_name=service,
        validate=True,
        metrics_factory=PrometheusMetricsFactory(service_name_label=service),
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer("backend")
flask_tracer = FlaskTracing(tracer, True, app)
parent_span = flask_tracer.get_span()

# Decorate function with metric.
@s.time()
@app.route("/")
def homepage():
    response = 'Hello World'

    with tracer.start_span('homepage', child_of=parent_span) as span:
        span.set_tag('message', response)
        return response

# Decorate function with metric.
@s.time()
@app.route("/api")
def my_api():
    answer = "something"

    with tracer.start_span('api', child_of=parent_span) as span:
        # add some delay
        for i in range(3):
            process_request_with_random_delay(random.random())

        span.set_tag('message', answer)
        return jsonify(response=answer)

# Decorate function with metric.
@s.time()
@c.count_exceptions()
@app.route("/star", methods=["POST"])
def add_star():
    output = {}

    with tracer.start_span('star') as span:
        try:
            star = mongo.db.stars

            name = request.json["name"]
            distance = request.json["distance"]
            star_id = star.insert({"name": name, "distance": distance})
            new_star = star.find_one({"_id": star_id})
            output = {"name": new_star["name"], "distance": new_star["distance"]}

            span.set_tag('output', output)
        except:
            span.set_tag('error', 'Error: Unable to process request')

    return jsonify({"result": output})

# Decorate function with metric.
@s.time()
def process_request_with_random_delay(t):
    """A dummy function that takes some time."""
    time.sleep(t)


# Register endpoint that returns 4xx error
@app.route("/client-error")
@metrics.summary('requests_by_status_4xx', 'Status Code', labels={
    'code': lambda r: '400'
})
def client_error():
    return "4xx Error", 400

# Register endpoint that returns 5xx error
@app.route("/server-error")
@metrics.summary('requests_by_status_5xx', 'Status Code', labels={
    'code': lambda r: '500'
})
def server_error():
    return "5xx Error", 500



if __name__ == "__main__":
    app.run()
