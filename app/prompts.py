SYSTEM_PROMPT = """You are a senior software engineer performing a strict code review.
You must be concise, practical, and helpful.
You output MUST be Markdown.
Focus on correctness, security, performance, maintainability, and testability.
"""


def build_user_prompt(diff_text: str) -> str:
    return f"""Review the following GitHub Pull Request diff.

Return a Markdown review with these sections:
1) Summary (2-4 bullets)
2) Key Risks (max 6 bullets)
3) Suggested Tests (unit/integration/e2e) (max 8 bullets)
4) Improvements (max 8 bullets)
5) Questions to the author (max 6 bullets)

Diff:
```diff
{diff_text}
```""".strip()
