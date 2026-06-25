# AI Courtroom Game

Project scaffold with a FastAPI backend and Next.js frontend.

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
