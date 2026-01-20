import os
from typing import Any

from flask import Flask, request, jsonify
from transformers import pipeline

model_path = os.path.join(os.path.dirname(__file__), "sentiment")

app = Flask(__name__)

pipe = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)


@app.route("/api/sentiment", methods=["POST"])
def make_prediction() -> Any:
    data = request.get_json(force=True)
    text = data["text"]
    result = pipe(text)
    return jsonify(result)


@app.route("/api/sentiment/batch", methods=["POST"])
def make_batch_prediction() -> Any:
    data = request.get_json(force=True)
    items = data["items"]

    texts = [x["text"] for x in items]
    results = pipe(texts)

    out = []
    for x, r in zip(items, results):
        out.append({"id": x.get("id"), **r})
    return jsonify({"results": out})


if __name__ == "__main__":
    app.run(port=9000, debug=True)
