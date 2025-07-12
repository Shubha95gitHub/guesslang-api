from flask import Flask, request, jsonify
from guesslang import Guess

app = Flask(__name__)
guess = Guess()  # Initialize the ML model

@app.route("/", methods=["GET"])
def home():
    return "ML-based Language Detection API is running"

@app.route("/detect", methods=["POST"])
def detect_language():
    data = request.get_json()
    code = data.get("code", "")
    language = guess.language_name(code)
    return jsonify({"language": language})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
