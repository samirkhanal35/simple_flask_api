import requests, json

data = {
    'name':"samir khanal",
}

response = requests.get("http://127.0.0.1:5000/message",params=data)
print(response.json())


