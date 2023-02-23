import requests
import api



def get_data(place, days = None):
    api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(api_url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = days * 8
    filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Ankara", days=3, kind="Temperature"))
