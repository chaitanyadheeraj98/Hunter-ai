import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_structured_resume(job_description: str, user_bio: str = "") -> str:
    prompt = f"""
You are a professional resume writer. Generate a tailored resume based on the job description below.

Job Description:
{job_description}

User Bio:
{user_bio}

Format it with the following sections:
- Name
- Title
- Summary
- Skills
- Experience
- Education

Keep it concise and targeted.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert resume generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message['content']
