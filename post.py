import requests

url = 'http://127.0.0.1:8000/api/v1/responder'
myobj = {
            "birth_date": "2023-02-17",
            "gender": "m"
        }

x = requests.post(url, data = myobj)

print(x.text)