#!/usr/bin/env python3
"""flask api"""
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """print message to root"""
    return "Welcome to the Flask API!"


@app.route('/data')
def username():
    """return username"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    """print ok"""
    return "OK"


@app.route('/users/<username>')
def route_user(username):
    """look for a username"""
    for user in users:
        if user == username:
            return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """add username"""
    json_data = request.get_json()

    username = json_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "username": username,
        "name": json_data.get("name", ""),
        "age": json_data.get("age", ""),
        "city": json_data.get("city", "")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
