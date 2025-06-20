import os
from dotenv import load_dotenv
import httpx

load_dotenv()

JSEARCH_URL = "https://jsearch.p.rapidapi.com/search"
JSEARCH_API_KEY = os.getenv("JSEARCH_API_KEY")
JSEARCH_API_HOST = "jsearch.p.rapidapi.com"

async def fetch_jobs(title: str = "software engineer", location: str = "new york"):
    params = {
        "query": f"{title} in {location}",
        "page": "1",
        "num_pages": "1"
    }

    headers = {
        "X-RapidAPI-Key": JSEARCH_API_KEY,
        "X-RapidAPI-Host": JSEARCH_API_HOST
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(JSEARCH_URL, params=params, headers=headers)

    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print("Error:", response.status_code, response.text)
        return []
