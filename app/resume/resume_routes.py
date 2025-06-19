from fastapi import APIRouter, Request, Form
from app.resume.resume_generator import generate_structured_resume

router = APIRouter()

@router.post("/generate-resume")
async def generate_resume(job_desc: str = Form(...), base_resume: str = Form("")):
    result = generate_structured_resume(job_desc, base_resume)
    return {"resume": result}
