
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = genai.Client() #it reads gemini keys

class GeminiRequest(BaseModel):
    prompt: str


@app.post("/ask-gemini") #We're sending a prompt to Gemini and asking it to generate a new response.
async def ask_gemini(data: GeminiRequest):

    response = await client.aio.models.generate_content(
        model="gemini-3.8-flash",
        contents=data.prompt
    )

    return {
        "question": data.prompt,
        "answer": response.text
    }