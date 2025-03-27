from flask import Flask, jsonify, render_template

app = Flask(__name__)

import psycopg2
import os

@app.route("/")
def index():
    return render_template("index.html")

# Database connection settings
DB_SETTINGS = {
    "dbname": "peakmap",
    "user": "andor",
    "password": "peakpass",
    "host": "localhost",
    "port": 5432
}

def get_peaks():
    try:
        conn = psycopg2.connect(**DB_SETTINGS)
        cur = conn.cursor()
        cur.execute("SELECT id, name, lat, lng, description, image_path FROM peaks")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        return [
            {
                "id": row[0],
                "name": row[1],
                "lat": row[2],
                "lng": row[3],
                "description": row[4],
                "image": row[5]
            } for row in rows
        ]
    except psycopg2.Error as e:
        print("X Database error:", e)
        return []
        
@app.route("/api/peaks")
def api_peaks():
    return jsonify(get_peaks())

if __name__ == "__main__":
    app.run(debug=True)