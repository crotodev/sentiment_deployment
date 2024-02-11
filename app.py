import os
import math

from flask import Flask, request, jsonify
from transformers import pipeline

model_path = os.path.join(os.path.dirname(__file__), "sentiment")

app = Flask(__name__)

pipe = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)


@app.route('/api', methods=['POST'])
def make_prediction():
    data = request.get_json(force=True)
    text = data['text']
    result = pipe(text)
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=9000, debug=True)
