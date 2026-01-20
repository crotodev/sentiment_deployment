import requests, json

# Test single prediction endpoint
url = "http://localhost:9000/api/sentiment"
data = json.dumps({"text": "I love you"})

r = requests.post(url, data)
print("Single prediction result:")
print(r.json())

# Test batch prediction endpoint
batch_url = "http://localhost:9000/api/sentiment/batch"
batch_data = json.dumps(
    {
        "items": [
            {"id": 1, "text": "I love you"},
            {"id": 2, "text": "This is terrible"},
            {"id": 3, "text": "Amazing product!"},
        ]
    }
)

r_batch = requests.post(batch_url, batch_data)
print("\nBatch prediction result:")
print(json.dumps(r_batch.json(), indent=2))
