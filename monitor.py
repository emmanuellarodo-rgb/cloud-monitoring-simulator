import random
import time
import json

def generate_metrics():
    while True:
        cpu_usage = random.randint(10, 100)

        data = {
            "cpu": cpu_usage,
            "timestamp": time.time()
        }

        with open("metrics.json", "w") as f:
            json.dump(data, f)

        time.sleep(5)
