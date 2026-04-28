# Slackbot

A multi-tenant Slack bot for Q&A, MCQ, and alerts management.

## Development Setup

1. Create `.env` from `.env.example`
2. Start services: `docker-compose up`
3. Run migrations: `alembic upgrade head`
4. Start app: `uvicorn app.main:app --reload`

## Project Structure

- `app/` - Main application code
- `alembic/` - Database migrations
- `scripts/` - Utility scripts
