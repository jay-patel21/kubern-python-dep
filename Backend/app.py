from flask import Flask, request, jsonify
import psycopg2
from google.cloud import storage
from flask_cors import CORS  # Import CORS
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Google Cloud Storage configuration
GCP_BUCKET_NAME = 'thursday-project'
GCP_CREDENTIALS_JSON = 'braided-upgrade-435523-j8-d7fd30ea3f8b.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GCP_CREDENTIALS_JSON

# PostgreSQL database connection (replace with your GCP details)
def get_db_connection():
    conn = psycopg2.connect(
        host="199.223.234.9",
        database="postgres",
        user="postgres",
        password="root"
    )
    return conn

# Function to create necessary tables
def create_tables():
    conn = get_db_connection()
    cur = conn.cursor()

    # Create users table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    ''')

    # Create posts table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            file_url TEXT NOT NULL
        )
    ''')

    conn.commit()
    cur.close()
    conn.close()

# Call the table creation function when the app starts
def initialize_app():
    create_tables()

# Route for user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data['username']
    password = data['password']  # No encryption as per your request

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "User registered successfully!"})

# Route for user login
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data['username']
    password = data['password']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Invalid username or password!"}), 401

# Route to upload file to GCP and store link in DB
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    # Upload the file to GCP
    storage_client = storage.Client()
    bucket = storage_client.bucket(GCP_BUCKET_NAME)
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

    # Store the file link in the PostgreSQL database
    file_url = f"https://storage.googleapis.com/{GCP_BUCKET_NAME}/{file.filename}"
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO posts (file_url) VALUES (%s)", (file_url,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "File uploaded successfully!", "file_url": file_url})

# Route to show all posts
@app.route('/posts', methods=['GET'])
def show_posts():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts")
    posts = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify({"posts": posts})

# New GET endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello"})

if __name__ == '__main__':
    initialize_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
