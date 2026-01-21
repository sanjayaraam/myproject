from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "SJ : MyProject : CI/CD enabled Kubernetes App"


@app.route("/health")
def health():
    """
    Health endpoint for Kubernetes readiness/liveness probes
    """
    return jsonify(
        status="UP",
        service="myproject",
        timestamp=datetime.utcnow().isoformat() + "Z"
    ), 200


@app.route("/info")
def info():
    """
    Shows runtime & deployment details
    Useful for debugging Kubernetes & CI/CD deployments
    """
    return jsonify(
        project="MyProject",
        owner="Sanjay Jayaram",
        environment=os.getenv("ENVIRONMENT", "local / kubernetes"),
        version=os.getenv("APP_VERSION", "unknown"),
        pod_name=os.getenv("HOSTNAME", socket.gethostname()),
        server_time=datetime.utcnow().isoformat() + "Z"
    )


@app.route("/about")
def about():
    """
    Explains what this project demonstrates
    """
    return jsonify(
        description="End-to-end DevOps & SRE practice project",
        features=[
            "GitHub Actions CI/CD",
            "Docker image build & push",
            "Kubernetes Deployment & Service",
            "Ingress routing",
            "GitOps-style Continuous Deployment",
            "Versioned Docker images",
            "Rollback via Git"
        ]
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
