# AI Courtroom Game

This is a project that simulates a Phoenix Wright Ace Attorney Game. <br />
It uses FastAPI for backend, and React/Next.js for frontend with Shadcn components. Cases and related information are stored in a SQLite database. Uses AI Agent SDK from Vercel to power the app.

## Demo 
[![AI Courtroom Game demo](https://img.youtube.com/vi/P8jSSm32L6s/maxresdefault.jpg)](https://youtu.be/P8jSSm32L6s)



## Environment

Set the model at AI_GATEWAY_MODEL i.e openai/gpt-4.1-mini

## Structure

```text
backend/
  app/
    api/
    core/
    db/
    models/
    schemas/
    services/
frontend/
  src/
    app/
    components/
    lib/
    types/
```

## Development

Start the backend:

```bash
cd backend
uv sync
uv run python -m app.db.init_db
uv run uvicorn app.main:app --reload
```

Start the frontend:

```bash
cd frontend
npm install
npm run dev
```
