from pydantic import BaseModel, Field

class ReviewRequest(BaseModel):
    pr_url: str = Field(..., example="https://github.com/OWNER/REPO/pull/123")

class ReviewResponse(BaseModel):
    pr_url: str
    markdown_review: str
