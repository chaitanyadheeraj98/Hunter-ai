from fastapi import APIRouter, Query
from typing import Optional
from app.jobs.jsearch_api import fetch_jobs

router = APIRouter()

@router.get("/")
async def get_jobs(
    title: Optional[str] = Query(None, description="Job title to search for"),
    location: Optional[str] = Query(None, description="Location to search in")
):
    jobs = fetch_jobs(title=title or "", location=location or "")
    return {"results": jobs}
