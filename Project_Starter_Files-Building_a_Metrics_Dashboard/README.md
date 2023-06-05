**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

![image](https://github.com/hungdq1379/CloudNative_Project3/assets/113217676/63aecbb6-1ea8-4f54-b94b-ddd696f3d704)

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
![image](https://github.com/hungdq1379/CloudNative_Project3/assets/113217676/09910478-d5b4-4b9c-9adb-ae54637b5938)

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
![image](https://github.com/hungdq1379/CloudNative_Project3/assets/113217676/a1b23335-5622-4d95-bd5d-a4cf04154f7a)

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.
A Service-Level Objective (SLO) is a measurable goal set by the SRE team to ensure a standard level of performance during a specified period of time.
For example, we might specify an SLO like "99.99% uptime per month". Typically SLOs are measured in terms of latency and uptime, although it is not unusual for SRE teams to add additional goals.
A Service-Level Indicator (SLI) is a specific metric used to measure the performance of a service.
For example, The application will have an uptime of 99.9% during the next year.
## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
- Site Latency/System Thoroughput measures the time it takes for some data to get to its destination across the network. It is usually measured as a round trip delay - the time taken for information to get to its destination and back again. The round trip delay is an important measure because a computer that uses a TCP/IP network sends a limited amount of data to its destination and then waits for an acknowledgement to come back before sending any more. Thus, the round trip delay has a key impact on the performance of the network. Latency drives the responsiveness of the network - how fast each conversation can be had. For TCP/IP networks, latency also drives the maximum throughput of a conversation.
- Network Uptime/Availability refers to the time when a network is up and running. A network’s uptime is typically measured by calculating the ratio of uptime to downtime within a year, then expressing that ratio as a percentage. The concept of “five-nines” — a network availability of 99.999% — has been an industry gold standard for many years, and this translates to about 5.26 minutes of unplanned downtime a year.
- Response Rate is the average time taken for successful requests of a service during a particular period. For example, your service will respond within one second for 99% of all requests.
- Error Rate is the percentage of acceptable errors within a given period. For example, a 1% error rate would result in an SLO at 99%, indicating that the customer is having a relatively error-free positive experience.
- The Bandwidth of a network refers to its capacity to carry traffic. A higher bandwidth means that more traffic can be carried. It does not imply how fast that communication will take place (although if you attempt to put more traffic over a network than the available bandwidth, you'll get packets of data being discarded and re-transmitted later, which will degrade your performance). Bandwidth limits the number of those conversations that can be supported.

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
