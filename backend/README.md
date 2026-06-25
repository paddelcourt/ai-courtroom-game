# AI Courtroom Game Backend

FastAPI backend scaffold with API, config, database, models, schemas, and services split into separate modules.

## Run locally

```bash
cd backend
uv sync
uv run python -m app.db.init_db
uv run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000/api/v1`.
