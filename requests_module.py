import requests

API_KEY = "5b9db5a78f026925a908412c759a8a47"
cityName = 'Mathura'
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={API_KEY}")

data = response.json()
print(data["weather"])
print(type(data["weather"]))
real_data = dict(data["weather"][0])
print(real_data)
print(real_data['description'])



# put requests 

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  }

response = requests.post(url=url,data = data)
print(response.text)