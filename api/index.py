# Contoh menggunakan Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Halo dari Python di Vercel!"

@app.route("/waktu")
def waktu():
    import datetime
    return f"Waktu server saat ini: {datetime.datetime.now()}"