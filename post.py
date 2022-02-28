import requests
from requests.auth import HTTPBasicAuth

url = 'http://127.0.0.1:8000/api/v1/BaseSubquestion/'
auth = HTTPBasicAuth('admin', 'qwerty')
myobj = {
            "question": "is it right?",
            "predefined_answer": "very"
         
        }

x = requests.post(url, data = myobj, auth=auth)

print(x.text)