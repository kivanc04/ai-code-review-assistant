import os
from openai import OpenAI
from .prompts import SYSTEM_PROMPT, build_user_prompt

def generate_review(diff_text: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY in environment")

    client = OpenAI(api_key=api_key)

    # Safety: diff çok büyük olursa kes
    max_chars = 14000
    if len(diff_text) > max_chars:
        diff_text = diff_text[:max_chars] + "\n\n... (diff truncated)"

    user_prompt = build_user_prompt(diff_text)

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )

    return resp.choices[0].message.content.strip()
