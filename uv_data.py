from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def uv_data_home():
    return render_template("uv_data_home.html")


@app.route('/uv_data_city', methods=['POST'])
def uv_data_city():

    city_name = request.form['name']

    if city_name == "London":
        lat = "51.75"
        lon = "-0.25"
    elif city_name == "Southampton":
        lat = "50.75"
        lon = "-1.25"
    elif city_name == "Bristol":
        lat = "51.25"
        lon = "2.75"
    else:
        lat = "50.75"
        lon = "-1.25"
        city_name = "Southampton"

    times = ["2016Z", "2017Z"]

    api_id = "7958e9414fd8326b21f164f691769641"
    api = 'http://api.openweathermap.org/v3/uvi/'

    uv_values = []

    for time in times:

        full_api_url = api + lat + "," + lon + "/" + time + ".json?appid=" + api_id

        print(full_api_url)

        request_data = requests.get(full_api_url)

        uv_values.append(json.loads(request_data.text)['data'])

    return render_template("uv_data_city.html", city_name=city_name.title(), uv2016=str(uv_values[0]).title(), uv2017=str(uv_values[1]).title())

if __name__ == "__main__":
    app.run()
