import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"


def fetch(endpoint, params):
    """Call the OpenWeatherMap API and return JSON."""
    response = requests.get(
        f"{BASE_URL}/{endpoint}",
        params={**params, "appid": API_KEY},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/weather")
def weather():
    city = request.args.get("city")
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    units = request.args.get("units", "metric")

    if city:
        params = {"q": city, "units": units}
    elif lat and lon:
        params = {"lat": lat, "lon": lon, "units": units}
    else:
        return jsonify(error="Please provide a city or location."), 400

    try:
        current = fetch("weather", params)
        forecast = fetch("forecast", params)
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            return jsonify(error="City not found."), 404
        return jsonify(error="Weather service error. Try again."), 502
    except requests.RequestException:
        return jsonify(error="Network problem. Try again."), 503

    # The forecast comes in 3-hour steps; keep one entry per day (noon)
    daily = [
        {
            "date": item["dt_txt"].split(" ")[0],
            "temp": round(item["main"]["temp"]),
            "description": item["weather"][0]["description"].title(),
            "icon": item["weather"][0]["icon"],
        }
        for item in forecast["list"]
        if item["dt_txt"].endswith("12:00:00")
    ]

    return jsonify(
        current={
            "city": current["name"],
            "country": current["sys"]["country"],
            "temp": round(current["main"]["temp"]),
            "feels_like": round(current["main"]["feels_like"]),
            "humidity": current["main"]["humidity"],
            "wind": current["wind"]["speed"],
            "description": current["weather"][0]["description"].title(),
            "icon": current["weather"][0]["icon"],
        },
        daily=daily,
    )


if __name__ == "__main__":
    app.run(debug=True)