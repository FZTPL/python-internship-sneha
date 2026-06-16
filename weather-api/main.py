from fastapi import FastAPI, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
import requests
import os
import redis
import json
from dotenv import load_dotenv

load_dotenv()

cache = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    decode_responses=True
)

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/")
def home():
    return {"message": "Weather API"}

def get_weather(city):
    api_key=os.getenv("WEATHER_API_KEY")
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={api_key}"
    response=requests.get(url)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )
    return response.json()

@app.get("/weather/{city}")
@limiter.limit("10/minute")
def weather(request: Request, city: str):
    cached_data = cache.get(city)
    if cached_data:
        return {
            "source": "cache",
            "data": json.loads(cached_data)
        }
    data = get_weather(city)
    weather_info = {
        "city": data["address"],
        "temperature": data["days"][0]["temp"]
    }

    cache.set(city, json.dumps(weather_info), ex=43200)

    return {
        "source": "api",
        "data": weather_info
    }