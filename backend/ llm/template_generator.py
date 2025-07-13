# llm/template_generator.py
import os
import requests
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("Please set the GEMINI_API_KEY environment variable")

GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def call_gemini_api(prompt: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(GEMINI_ENDPOINT, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"GEMINI API Error: {response.text}")
    data = response.json()
    return data['candidates'][0]['content']['parts'][0]['text']

def generate_template(issue_text: str, criticality: str) -> str:
    prompt = f"""A customer raised an issue:
'{issue_text}'
The criticality level is: {criticality}.
Write a professional, helpful support message that can be sent to the customer."""
    return call_gemini_api(prompt)
