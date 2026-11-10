# Weather Forecast App

A Flask web app that shows real-time weather and a 5-day forecast, with automatic location detection.

## Features
- Search weather by city
- Auto-detect your location (browser geolocation)
- Current conditions plus 5-day forecast
- Celsius/Fahrenheit toggle
- Error handling for invalid cities and network issues

## Tech Stack
Python, Flask, OpenWeatherMap API, HTML, CSS, JavaScript

## Setup
1. Clone the repo:
   `git clone https://github.com/IpshitaShrivastava/weather-forecast-app.git`
2. Go into the folder and create a virtual environment:
   `python3 -m venv venv` then `source venv/bin/activate`
3. Install packages: `pip install -r requirements.txt`
4. Create a `.env` file containing: `OPENWEATHER_API_KEY=your_key_here`
5. Run the app: `python app.py`
6. Open http://127.0.0.1:5000

## Live Demo
Link coming soon.

*Built as part of my Python Development internship at Pinnacle Labs.*