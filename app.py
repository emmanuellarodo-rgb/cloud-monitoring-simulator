from flask import Flask, jsonify
import threading
from monitor import generate_metrics
from scaler import check_scale
import json

app = Flask(__name__)

# Background monitoring
threading.Thread(target=generate_metrics, daemon=True).start()

@app.route("/")
def home():
    return "Cloud Monitoring Simulator Running 🚀"

@app.route("/metrics")
def metrics():
    try:
        with open("metrics.json") as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return jsonify({"error": "No data"})

@app.route("/scale")
def scale():
    decision = check_scale()
    return jsonify({"decision": decision})

if __name__ == "__main__":
    app.run(port=5000)
