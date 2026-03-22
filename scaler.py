import json

def check_scale():
    try:
        with open("metrics.json") as f:
            data = json.load(f)

        cpu = data["cpu"]

        if cpu > 70:
            return "Scale UP 🚀"
        elif cpu < 30:
            return "Scale DOWN ⬇️"
        else:
            return "Stable ✅"

    except:
        return "No data"
