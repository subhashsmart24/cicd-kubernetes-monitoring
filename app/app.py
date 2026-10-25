import time

from flask import Flask, g, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "http_status"],
)

REQUEST_LATENCY = Histogram(
    "app_http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["endpoint"],
)


@app.before_request
def start_timer():
    g.start_time = time.time()


@app.after_request
def record_metrics(response):
    endpoint = request.endpoint or "unknown"
    duration = time.time() - getattr(g, "start_time", time.time())

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint,
        http_status=response.status_code,
    ).inc()

    REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)

    return response


@app.route("/")
def home():
    return jsonify(
        {
            "application": "DevOps CI/CD Monitoring Demo",
            "version": "1.0.0",
            "status": "running",
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/metrics")
def metrics():
    return (
        generate_latest(),
        200,
        {"Content-Type": CONTENT_TYPE_LATEST},
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)