from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

from .schemas import ReviewRequest, ReviewResponse
from .github_client import fetch_pr_diff
from .llm import generate_review

load_dotenv()

app = FastAPI(title="AI Code Review Assistant", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/review", response_model=ReviewResponse)
async def review(req: ReviewRequest):
    try:
        diff_text = await fetch_pr_diff(req.pr_url)
        markdown = generate_review(diff_text)
        return ReviewResponse(pr_url=req.pr_url, markdown_review=markdown)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
