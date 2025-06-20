import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY is not set.")

openai.api_key = api_key

async def generate_structured_resume(job_description: str, user_bio: str = "") -> str:
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

    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",  # Use GPT-4 if accessible
            messages=[
                {"role": "system", "content": "You are an expert resume generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.get('content', '')
    except Exception as e:
        print("Error during OpenAI call:", e)
        raise
