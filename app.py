from flask import Flask, request, jsonify
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Language Detection API is running"

@app.route("/detect", methods=["POST"])
def detect_language():
    data = request.get_json()
    code = data.get("code", "")

    try:
        lexer = guess_lexer(code)
        return jsonify({"language": lexer.name})
    except ClassNotFound:
        return jsonify({"language": "Unknown"}), 400

if __name__ == "__main__":
    app.run()
