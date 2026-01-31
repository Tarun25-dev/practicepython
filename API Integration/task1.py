"""
First you need to create a database called college in MySQL
Ex:
CREATE DATABASE college;
USE college;

Next create a student table inside college database
"USE college"

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    branch VARCHAR(50)
);

Install MySQL interacting module for python
pip install flask mysql-connector-python
"""

"""
Example API creation:

from flask import Flask, request, jsonify
# request - used to read data sent by the client (POST/JSON data)
# jsonify - converts Python data (dict/list) into JSON response
import mysql.connector # Used to connect Flask with MySQL database

app = Flask(__name__)
# app → main Flask application object
# __name__ tells Flask:
# “This file is the main file”

# Database connection
def get_db_connection():
# reuse MySQL connection code,Avoids writing connection logic again and again
    return mysql.connector.connect( # Creates and returns a MySQL connection object
        host="localhost",
        user="root",
        password="your_password",
        database="college"
    )

# ----------------------------
# READ API (GET)
# ----------------------------
@app.route("/students", methods=["GET"])

# Defines an API endpoint
# URL: http://127.0.0.1:5000/students
# Method: GET
# Purpose: fetch students data
# This is called a REST API route

def get_students():
# Function that runs when /students is called with GET
    conn = get_db_connection()
    # Calls DB function, Opens MySQL connection
    
    cursor = conn.cursor(dictionary=True)
    # Cursor is used to execute SQL queries
    # it returns tuple but we need in dict just like json format
    # dictionary=True means:
    # Result will be returned as:
    # {"id": 1, "name": "Tarun", "branch": "ISE"}

    cursor.execute("SELECT * FROM students")
    # Executes SQL query, Fetches all records from students table
    
    students = cursor.fetchall()
    # Fetches all rows
    # Stores them as a Python list of dictionaries

    cursor.close()
    conn.close()
    # Closes cursor and DB connection
    # Prevents memory leaks
    
    return jsonify(students)
    # Converts Python list → JSON
    # Sends response to client

# ----------------------------
# CREATE API (POST)
# ----------------------------
@app.route("/students", methods=["POST"])
# Same URL /students
# Different method → POST
# Used to insert new student

def add_student():
    data = request.json
    name = data["name"]
    branch = data["branch"]
    # Extract values from JSON

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, branch) VALUES (%s, %s)",
        (name, branch)
    )
    # Executes SQL INSERT query
    # %s → prevents SQL Injection
    # Values safely passed as tuple
    
    conn.commit()
    # Saves changes to database
    # Without commit → data won't be inserted
    
    cursor.close()
    conn.close()

    return jsonify({"message": "Student added successfully"}), 201
    # Sends success message
    # 201 → HTTP status code for Created
# HTTP status codes tell the client what happened to the request, without reading the response body.
if __name__ == "__main__":
    app.run(debug=True)

"""