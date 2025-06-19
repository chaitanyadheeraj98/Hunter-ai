from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# You can import your route handlers here if any
from app.jobs import job_routes #, ai_routes, notify_routes

def create_app() -> FastAPI:
    app = FastAPI(
        title="Hunter AI",
        description="AI-powered job hunter and resume customizer",
        version="1.0.0",
    )

    # CORS Middleware (for frontend interaction or browser API calls)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Change to ["https://yourdomain.com"] in prod
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    async def health_check():
        return {"status": "ok"}
    
    @app.get("/")
    async def root():
        return {"message": "Hunter AI is running"}


    # Register routers (add actual routers later)
    app.include_router(job_routes.router, prefix="/jobs")
    # app.include_router(ai_routes.router, prefix="/ai")
    # app.include_router(notify_routes.router, prefix="/notify")

    return app

app = create_app()