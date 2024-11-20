from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS
from dotenv import load_dotenv
import os
# connection = mysql.connect(host="localhost",user= "release_user", password ="release_password",database ="api_user_detail")
app = Flask(__name__)
CORS(app)

load_dotenv()

# Connect to MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return conn

# Create a new post
@app.route('/api/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Post created successfully'}), 201

@app.route("/api/table_detail")
def get_table_details():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * from posts;")
    return jsonify({"Details":  [{"id": post[0], "title": post[1], "content": post[2]} for post in cursor.fetchall()] })
    


if __name__ == '__main__':
    app.run(debug=True)