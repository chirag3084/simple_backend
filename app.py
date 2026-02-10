from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend requests

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Backend is running"
    })

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "text field missing"}), 400

    text = data["text"]

    # simple logic (replace with AI later)
    result = {
        "original_text": text,
        "length": len(text),
        "uppercase": text.upper()
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
