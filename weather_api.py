import requests

api_key = "7fd72c05dcad723e5d7966a0f397b262"  # your active key
city = "Paris"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

print("Requesting:", url)  # shows the full API URL

response = requests.get(url)

print("Status Code:", response.status_code)  # shows HTTP code

if response.status_code == 200:
    data = response.json()
    print(f"City : {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Error fetching weather data.")
    print("Response Text:", response.text)



