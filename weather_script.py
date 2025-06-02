import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]['description']
        temp = main['temp']
        return f"Weather in {city}: {weather}, Temperature: {temp}°C"
    else:
        return "Error fetching weather data."

        if __name__ == "__main__":
            city = input("Enter city name: ")
            api_key = input("Enter your OpenWeatherMap API key: ")
            print(get_weather(city, api_key))