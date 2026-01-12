"""
File Name: app.py
Purpose:
This file demonstrates the basics of building a REST API using Flask.
It includes simple GET and POST endpoints to understand how APIs work.
This project is suitable for beginners and for GitHub portfolio upload.
"""

# Import Flask class from flask module
from flask import Flask, jsonify, request

# Create a Flask application instance
app = Flask(__name__)

# -------------------------------
# Basic GET API (Home Route)
# -------------------------------
# This route is used to check whether the API is running or not
@app.route('/', methods=['GET'])
def home():
    # Return a JSON response with a success message
    return jsonify({
        "message": "Welcome to Flask API Basics",
        "status": "API is running successfully"
    })


# -------------------------------
# GET API to fetch user data
# -------------------------------
@app.route('/user', methods=['GET'])
def get_user():
    # Sample user data (normally this comes from database)
    user_data = {
        "name": "Danish",
        "role": "AI & ML Student",
        "skills": ["Python", "Machine Learning", "Flask"]
    }

    # Send user data as JSON response
    return jsonify(user_data)


# -------------------------------
# POST API to receive data
# -------------------------------
@app.route('/add-data', methods=['POST'])
def add_data():
    # Get JSON data sent by the client
    data = request.get_json()

    # Extract values from JSON input
    name = data.get("name")
    course = data.get("course")

    # Return received data as confirmation
    return jsonify({
        "message": "Data received successfully",
        "name": name,
        "course": course
    })


# -------------------------------
# Run the Flask application
# -------------------------------
if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
