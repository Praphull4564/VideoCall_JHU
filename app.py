from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Video call by yadav jiii"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///video-meeting.db"
db = SQLAlchemy(app)

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return redirect(url_for("join"))

@app.route("/meeting/<room_id>")
def meeting(room_id):
    return render_template("meeting.html", room_id=room_id)

@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        room_id = request.form.get("roomID")
        return redirect(url_for("meeting", room_id=room_id))
    return render_template("join.html")

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')  # For self-signed certificates
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=context)
