import os
import re
import httpx

GITHUB_API = "https://api.github.com"


def parse_pr_url(pr_url: str):
    """
    Example:
    https://github.com/OWNER/REPO/pull/123
    """
    m = re.match(r"https://github\.com/([^/]+)/([^/]+)/pull/(\d+)", pr_url)
    if not m:
        raise ValueError("Invalid PR URL format. Use: https://github.com/OWNER/REPO/pull/NUMBER")
    owner, repo, pr_number = m.group(1), m.group(2), int(m.group(3))
    return owner, repo, pr_number


async def fetch_pr_diff(pr_url: str) -> str:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("Missing GITHUB_TOKEN in environment")

    owner, repo, pr_number = parse_pr_url(pr_url)

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3.diff",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "ai-code-review-assistant",
    }

    url = f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pr_number}"

    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        r = await client.get(url, headers=headers)
        r.raise_for_status()
        return r.text
