from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Student Backend is Running!"

@app.route("/student")
def student():
    return jsonify({
        "name": "Anu",
        "department": "Information Technology",
        "year": "III Year"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)