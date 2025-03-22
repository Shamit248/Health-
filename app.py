from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load JSON data
def load_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# API to fetch medicine details
@app.route("/search", methods=["GET"])
def search_medicine():
    query = request.args.get("name", "").strip().lower()
    medicines = load_json()["medicines"]

    for medicine in medicines:
        if medicine["name"].strip().lower() == query:
            return jsonify(medicine)

    return jsonify({"error": "Medicine not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
