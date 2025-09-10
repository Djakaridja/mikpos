from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from .db import init_engine, create_session_factory
from sqlalchemy import text


def get_cors_origins() -> list[str]:
    origins = os.getenv("CORS_ORIGINS", "").split(",")
    origins = [o.strip() for o in origins if o.strip()]
    if not origins:
        origins = ["*"]
    return origins


app = FastAPI(title="App Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database setup
engine = init_engine()
SessionLocal = create_session_factory(engine)


@app.get("/health")
def health() -> dict[str, str]:
    try:
        with engine.connect() as conn:
            conn.execute(text("select 1"))
        return {"status": "ok"}
    except Exception:
        return {"status": "degraded"}

