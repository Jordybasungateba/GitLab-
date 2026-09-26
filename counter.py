from flask import Flask
import status

app = Flask(__name__)
COUNTERS = {}
@app.route("/counter/<name>", methods=["POST"])
def create_counter(name):
    app.logger.info(f"Creating counter: {name}")
    if name in COUNTERS:
        return {"error": "Counter already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED