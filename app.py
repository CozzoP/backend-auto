from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(os.environ["DATABASE_URL"])

@app.route("/auto", methods=["GET"])
def get_auto():
    cur = conn.cursor()
    cur.execute("SELECT marca, modello FROM auto")
    rows = cur.fetchall()
    return jsonify(rows)

@app.route("/auto", methods=["POST"])
def add_auto():
    data = request.json
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO auto (marca, modello) VALUES (%s, %s)",
        (data["marca"], data["modello"])
    )
    conn.commit()
    return {"status": "ok"}

app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
