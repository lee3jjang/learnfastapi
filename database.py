from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


__all__ = [
    "Base",
    "SessionLocal",
]

SQLALCHEMY_DATABASE_URL = "sqlite:///./learnfastapi.db"

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
