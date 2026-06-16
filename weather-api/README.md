# Weather API

A RESTful Weather API built using FastAPI that fetches weather data from the Visual Crossing Weather API and caches responses using Redis for improved performance.

## Features

* Fetch real-time weather information by city
* Redis caching to reduce external API calls
* Automatic cache expiration (12 hours)
* Rate limiting to prevent abuse
* Environment variable configuration
* Error handling for invalid cities and API failures
* FastAPI automatic API documentation

## Technologies Used

* Python
* FastAPI
* Redis
* Requests
* Python Dotenv
* SlowAPI (Rate Limiting)

## Project Structure

```text
weather-api/
│
├── main.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### Clone the Repository

```bash
git clone <your-repository-url>
cd weather-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory.

```env
WEATHER_API_KEY=your_visual_crossing_api_key

REDIS_HOST=localhost
REDIS_PORT=6379
```

## Running Redis

Start Redis locally:

```bash
redis-server
```

Verify Redis is running:

```bash
redis-cli ping
```

Expected output:

```text
PONG
```

## Running the Application

```bash
uvicorn main:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "Weather API"
}
```

### Get Weather by City

```http
GET /weather/{city}
```

Example:

```http
GET /weather/kathmandu
```

Response:

```json
{
  "source": "api",
  "data": {
    "city": "kathmandu",
    "temperature": 76.4,
    "conditions": "Partially cloudy"
  }
}
```

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

## Caching Strategy

* Weather data is stored in Redis.
* City name is used as the cache key.
* Cached data expires automatically after 12 hours.
* Repeated requests for the same city are served from cache instead of calling the external weather API.

## Rate Limiting

The API uses SlowAPI for rate limiting.

Current configuration:

```text
10 requests per minute per client
```

Requests exceeding this limit will receive an error response.

## Error Handling

The API handles:

* Invalid city names
* Failed third-party API requests
* Redis connection errors
* Rate limit violations

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Learning Outcomes

This project demonstrates:

* REST API development with FastAPI
* Third-party API integration
* Redis caching
* Environment variable management
* Rate limiting
* Error handling
* JSON data processing
* API documentation

## Future Improvements

* Pydantic response models
* Docker support
* Unit testing
* PostgreSQL integration
* User authentication
* Weather forecast endpoints

## License

This project is created for learning and educational purposes.
