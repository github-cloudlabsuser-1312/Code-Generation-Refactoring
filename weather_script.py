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

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    print("Basic Calculator")
    print("Type 'weather' to fetch weather data.")
    choice = input("Choose 'calc' for calculator or 'weather': ").strip().lower()
    if choice == 'weather':
        city = input("Enter city name: ")
        api_key = input("Enter your OpenWeatherMap API key: ")
        print(get_weather(city, api_key))
    else:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operator"

        print("Result:", result)