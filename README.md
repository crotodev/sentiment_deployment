# Sentiment Analysis API

A Flask-based REST API for sentiment analysis using a pre-trained transformer model. The API provides both single and batch prediction endpoints for analyzing the sentiment of text inputs.

## Features

- **Single Prediction**: Analyze sentiment for individual text inputs
- **Batch Prediction**: Analyze sentiment for multiple texts in a single request
- **Production Ready**: Configured with Gunicorn for production deployment
- **Pre-trained Model**: Uses a locally stored sentiment analysis model from Hugging Face Transformers

## Prerequisites

- Python 3.11
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sentiment_deployment
```

2. Create and activate a virtual environment:
```bash
python3.11 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

**Note**: If you encounter NumPy version compatibility issues, downgrade NumPy:
```bash
pip install 'numpy<2'
```

## Project Structure

```
sentiment_deployment/
├── app.py                 # Flask application with API endpoints
├── main.py               # Test script for the API
├── gunicorn_config.py    # Gunicorn configuration for production
├── requirements.txt      # Python dependencies
├── sentiment/           # Pre-trained model directory
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── ...
└── README.md
```

## Usage

### Development Server

Start the Flask development server:

```bash
python app.py
```

The API will be available at `http://localhost:9000`

### Production Server

For production deployment, use Gunicorn:

```bash
gunicorn -c gunicorn_config.py app:app
```

## API Endpoints

### 1. Single Sentiment Analysis

**Endpoint**: `POST /api/sentiment`

**Request Body**:
```json
{
  "text": "I love this product!"
}
```

**Response**:
```json
[
  {
    "label": "POSITIVE",
    "score": 0.9998
  }
]
```

### 2. Batch Sentiment Analysis

**Endpoint**: `POST /api/sentiment/batch`

**Request Body**:
```json
{
  "items": [
    {"id": 1, "text": "I love you"},
    {"id": 2, "text": "This is terrible"},
    {"id": 3, "text": "Amazing product!"}
  ]
}
```

**Response**:
```json
{
  "results": [
    {"id": 1, "label": "POSITIVE", "score": 0.9998},
    {"id": 2, "label": "NEGATIVE", "score": 0.9995},
    {"id": 3, "label": "POSITIVE", "score": 0.9999}
  ]
}
```

## Testing

Run the included test script to verify the API is working:

```bash
python main.py
```

This will test both the single and batch prediction endpoints and display the results.

## Configuration

### Gunicorn Configuration

The `gunicorn_config.py` file supports the following environment variables:

- `GUNICORN_PROCESSES`: Number of worker processes (default: 2)
- `GUNICORN_THREADS`: Number of threads per worker (default: 4)
- `GUNICORN_BIND`: Bind address (default: 0.0.0.0:9000)

Example:
```bash
export GUNICORN_PROCESSES=4
export GUNICORN_THREADS=2
gunicorn -c gunicorn_config.py app:app
```

## Model

The application uses a pre-trained sentiment analysis model stored in the `sentiment/` directory. The model is loaded using the Hugging Face Transformers library's `pipeline` API.

## Dependencies

Key dependencies include:
- Flask 3.0.2 - Web framework
- transformers 4.37.2 - Hugging Face Transformers library
- torch 2.2.0 - PyTorch for model inference
- gunicorn 21.2.0 - Production WSGI server
- numpy 1.26.4 - Numerical computing

See `requirements.txt` for the complete list.

## Troubleshooting

### NumPy Version Compatibility

If you see errors about NumPy 1.x vs 2.x compatibility:
```bash
pip install 'numpy<2'
```

### Connection Refused Errors

Make sure the server is running before executing test scripts:
```bash
# Terminal 1
python app.py

# Terminal 2
python main.py
```

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
