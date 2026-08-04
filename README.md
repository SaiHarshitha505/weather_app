# 🌦 Weather Forecast Web Application

A full-stack Weather Forecast Web Application developed using **Python, Flask, SQLite, HTML, CSS, Bootstrap, and OpenWeather API**. This application allows users to register, log in, search for the weather of any city, and view a **5-day weather forecast** with a temperature graph.

---

## 📌 Project Overview

The Weather Forecast Web Application provides real-time weather information using the OpenWeather API. Users must create an account and log in before accessing the dashboard. The application displays the current weather details along with a graphical 5-day temperature forecast.

---

## ✨ Features

- User Registration (Signup)
- User Login & Logout
- Secure User Authentication
- Search Weather by City
- Current Temperature
- Humidity
- Weather Condition
- 5-Day Weather Forecast
- Temperature Graph using Matplotlib
- Responsive Bootstrap UI
- SQLite Database
- Error Handling for Invalid City Names

---

## 🛠 Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap 5

### Backend
- Python
- Flask

### Database
- SQLite

### Libraries
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Requests
- Matplotlib
- Gunicorn

---

## 📁 Project Structure

```
Weather_Forecast_Web_App/
│
├── app.py
├── requirements.txt
├── README.md
├── users.db
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── index.html
│
├── static/
│   ├── graph.png
│   ├── css/
│   └── images/
│
└── screenshots/
    ├── login.png
    ├── signup.png
    ├── dashboard.png
    └── forecast.png
```

---

## ⚙ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/weather-forecast-web-app.git
```

### Step 2: Open the Project Folder

```bash
cd weather-forecast-web-app
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Get an OpenWeather API Key

1. Create an account on OpenWeather.
2. Generate a free API key.
3. Open **app.py**.
4. Replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual API key.

### Step 5: Run the Application

```bash
python app.py
```

### Step 6: Open in Browser

```
http://127.0.0.1:5000
```

---

## 🚀 How the Application Works

### 1. Signup

- Create a new account.
- User details are stored in the SQLite database.

### 2. Login

- Login using your username and password.
- After successful login, the Weather Dashboard opens.

### 3. Search Weather

Enter a city name.

The application displays:

- City Name
- Temperature
- Humidity
- Weather Condition

### 4. View Forecast

The application fetches the next 5-day forecast and generates a temperature graph using Matplotlib.

---

## 📷 Screenshots

Add screenshots in the **screenshots** folder.

Example:

- Login Page
- Signup Page
- Weather Dashboard
- Weather Search Result
- Forecast Graph

---

## 📈 Future Enhancements

- Password Hashing
- Forgot Password
- GPS Location Detection
- Favorite Cities
- Search History
- Dark Mode
- Hourly Forecast
- Weather Alerts
- Email Notifications
- Cloud Deployment

---

## 💻 Requirements

- Python 3.10+
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Requests
- Matplotlib

Install all packages using:

```bash
pip install -r requirements.txt
```

---

## 📚 Learning Outcomes

Through this project, you will learn:

- Flask Web Development
- REST API Integration
- SQLite Database
- User Authentication
- Graph Generation with Matplotlib
- Responsive Web Design
- Python Backend Development

---

## 👩‍💻 Author

**M. Harshita**

B.Tech – Computer Science Engineering

Presidency University, Bangalore

---

## ⭐ Project Highlights

- Full-Stack Flask Application
- Login Authentication
- Weather API Integration
- SQLite Database
- Dynamic Weather Forecast
- Temperature Graph Visualization
- Responsive Bootstrap Interface
- Beginner-Friendly Project

---

## 📜 License

This project is created for educational and internship purposes. Feel free to use, modify, and enhance it for learning.
