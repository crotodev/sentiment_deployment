import requests, json

url = 'http://localhost:9090/api'
data = json.dumps({'text': 'I love you'})

r = requests.post(url, data)
print(r.json())