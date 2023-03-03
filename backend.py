import requests

API_KEY = "4b63b6ab44b802032a14d74405afbe71"


def get_data(place, forecast_days=2, type_of_data='Sky'):
    url = "http://api.openweathermap.org/data/2.5/" \
          f"forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8 * forecast_days]
    if type_of_data == "Temperature":
        filtered_data = [data_set["main"]["temp"] for data_set in filtered_data]
    if type_of_data == "Sky":
        filtered_data = [data_set["weather"][0]["main"] for data_set in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="tokyo"))
