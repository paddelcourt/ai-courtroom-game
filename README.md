# AI Courtroom Game

This is a project that simulates. It uses FastAPI for backend, and React/Next.js for frontend with Shadcn components. Cases and related information are stored in a database.

## Structure

```text
backend/
  app/
    api/
      cases.py
      health.py
      router.py
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
