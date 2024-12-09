from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data=get_current_weather(city)
    if not weather_data['cod']==200:
        return render_template(
            "city-not-found.html"
        )
    temp=float(weather_data['main']['temp']),
    feels_like=float(weather_data['main']['feels_like'])
    
    temp=(temp[0]-32)* (5/9)
    feels_like=(feels_like-32)*(5/9)
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{temp:.1f}",
        feels_like=f"{feels_like:.1f}"
    )

if __name__ == "__main__":
    serve(app,host="0.0.0.0",port=8000)