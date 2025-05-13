# app.py

from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open("data/summary.json") as f:
        summary = json.load(f)
    return render_template("index.html", summary=summary)

@app.route("/api/summary")
def api_summary():
    with open("data/summary.json") as f:
        summary = json.load(f)
    return jsonify(summary)

@app.route("/api/title/<int:title_id>")
def api_title(title_id):
    try:
        with open(f"data/parsed/title_{title_id}.json") as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Title not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route("/")
# def home():
    # return jsonify(message="Hello from eCFR Project Backend!")

# if __name__ == "__main__":
    # app.run(debug=True)
