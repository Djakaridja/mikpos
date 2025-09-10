import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


def get_database_url() -> str:
    default_url = "postgresql+psycopg2://app:app@db:5432/app"
    return os.getenv("DATABASE_URL", default_url)


def init_engine() -> Engine:
    database_url = get_database_url()
    connect_args = {}
    engine = create_engine(database_url, pool_pre_ping=True, connect_args=connect_args)
    return engine


def create_session_factory(engine: Engine) -> sessionmaker:
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

