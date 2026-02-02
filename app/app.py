from flask import Flask, jsonify, render_template
import os, socket, time
from datetime import datetime

app = Flask(__name__)
start_time = time.time()

@app.route("/")
def dashboard():
    return render_template(
        "index.html",
        project="MyProject",
        owner="Sanjay Jayaram",
        environment=os.getenv("ENVIRONMENT", "local"),
        version=os.getenv("APP_VERSION", "v1.0.0"),
        pod_name=os.getenv("HOSTNAME", socket.gethostname()),
        uptime=int(time.time() - start_time)
    )

@app.route("/health")
def health():
    return jsonify(
        status="UP",
        timestamp=datetime.utcnow().isoformat() + "Z"
    )

@app.route("/info")
def info():
    return jsonify(
        project="MyProject",
        owner="Sanjay Jayaram",
        environment=os.getenv("ENVIRONMENT", "kubernetes"),
        version=os.getenv("APP_VERSION", "unknown"),
        pod_name=os.getenv("HOSTNAME", socket.gethostname()),
        server_time=datetime.utcnow().isoformat() + "Z"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
