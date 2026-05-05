import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not set in environment")


def call_llm(prompt: str) -> str:

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": "You are a procurement assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=1,
    )

    return str(response.choices[0].message.content)
