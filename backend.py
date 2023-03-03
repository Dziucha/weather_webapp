import requests

API_KEY = "4b63b6ab44b802032a14d74405afbe71"


def get_data(place, forecast_days):
    url = "http://api.openweathermap.org/data/2.5/" \
          f"forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8 * forecast_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="tokyo"))
