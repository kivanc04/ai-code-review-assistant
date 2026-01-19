# AI Code Review Assistant

A FastAPI-based developer tool that takes a GitHub Pull Request URL, fetches the PR diff, and generates a strict, structured AI-powered code review in Markdown.

## Features
- Fetches PR diffs via GitHub API
- Generates a structured Markdown review:
  - Summary
  - Key Risks
  - Suggested Tests
  - Improvements
  - Questions to the Author
- Swagger UI for testing (`/docs`)
- Health endpoint (`/health`)

## Tech Stack
Python, FastAPI, GitHub REST API, OpenAI API, httpx

## Setup

### 1) Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

PR test change
