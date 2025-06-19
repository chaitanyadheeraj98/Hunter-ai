import uvicorn
from app import create_app  # This assumes your __init__.py is inside a folder named 'app'

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# For production, you might want to use a different server like Gunicorn or Daphne
# or run it behind a reverse proxy like Nginx.
