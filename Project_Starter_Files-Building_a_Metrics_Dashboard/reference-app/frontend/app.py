from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("main.html")

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
