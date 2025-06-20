from fastapi import APIRouter
from pydantic import BaseModel
from app.resume.resume_generator import generate_structured_resume

router = APIRouter()

class ResumeRequest(BaseModel):
    job_desc: str
    base_resume: str = ""

@router.post("/generate_resume")
async def generate_resume(data: ResumeRequest):
    result = generate_structured_resume(data.job_desc, data.base_resume)
    return {"resume": result}
