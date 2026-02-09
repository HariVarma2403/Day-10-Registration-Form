from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.json

    username = data.get("username")
    email = data.get("email")

    if len(username) < 4:
        return jsonify({"status": "error", "message": "Username too short"}), 400

    if not email.endswith("@gmail.com"):
        return jsonify({"status": "error", "message": "Invalid email"}), 400

    return jsonify({"status": "success", "message": "Registration successful"}), 200

if __name__ == "__main__":
    app.run(debug=True)
