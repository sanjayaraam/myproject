from flask import Flask, jsonify, render_template
import os, socket, time, psutil
from datetime import datetime

app = Flask(__name__)
start_time = time.time()

# ---------- UI ROUTES ----------
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/metrics-ui")
def metrics_ui():
    return render_template("metrics.html")

@app.route("/build-ui")
def build_ui():
    return render_template("build.html")

@app.route("/about")
def about():
    return render_template("about.html")

# ---------- API ROUTES ----------
@app.route("/api/health")
def health():
    return jsonify(status="UP")

@app.route("/api/info")
def info():
    return jsonify(
        project="MyProject",
        environment=os.getenv("ENVIRONMENT", "local"),
        version=os.getenv("APP_VERSION", "v1"),
        pod=os.getenv("HOSTNAME", socket.gethostname()),
        uptime=int(time.time() - start_time)
    )

@app.route("/api/metrics")
def metrics():
    return jsonify(
        cpu=psutil.cpu_percent(interval=0.5),
        memory=psutil.virtual_memory().percent
    )

@app.route("/api/build")
def build():
    return jsonify(
        git_commit=os.getenv("GIT_COMMIT", "unknown"),
        build_time=os.getenv("BUILD_TIME", "N/A"),
        image_version=os.getenv("APP_VERSION", "latest")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
