from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.secret_key = "secret123"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

API_KEY = "YOUR_API_KEY"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()

    temps, dates = [], []
    if "list" in data:
        for i in range(0, 40, 8):
            temps.append(data["list"][i]["main"]["temp"])
            dates.append(data["list"][i]["dt_txt"].split()[0])
    return temps, dates

def create_graph(temps, dates):
    if not temps:
        return None
    if not os.path.exists("static"):
        os.makedirs("static")

    plt.figure()
    plt.plot(dates, temps, marker='o')
    plt.title("5-Day Forecast")
    plt.xlabel("Date")
    plt.ylabel("Temp (°C)")
    plt.xticks(rotation=30)

    path = "static/graph.png"
    plt.savefig(path)
    plt.close()
    return path

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    weather = None
    graph = None
    error = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if "main" in data:
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"]
            }
            temps, dates = get_forecast(city)
            graph = create_graph(temps, dates)
        else:
            error = "City not found!"

    return render_template("index.html", weather=weather, graph=graph, error=error)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and user.password == request.form["password"]:
            login_user(user)
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        existing = User.query.filter_by(username=request.form["username"]).first()
        if existing:
            return "User already exists!"
        new_user = User(username=request.form["username"], password=request.form["password"])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
