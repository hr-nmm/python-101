from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your browser details are => {}</p>".format(user_agent)


@app.route("/user/<name>")
def user(name):
    data = {"user_id": 123, "user_name": name, "email": f"{name}@gmail.com"}
    return jsonify(data), 200
