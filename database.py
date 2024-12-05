# app/database.py
from sqlmodel import create_engine, SQLModel
from contextlib import asynccontextmanager

from app.models.author import Author
from app.models.book import Book

# Database URL (PostgreSQL)
postgresql_url = "postgresql://postgres:postgres@localhost:5432/bookAuthor"

# Create the engine
engine = create_engine(postgresql_url,echo=True)

# Create database tables
def create_db_and_tables():
    # SQLModel.metadata.create_all
    Author.metadata.create_all(bind=engine)
    Book.metadata.create_all(bind=engine)

# Session management (dependency)
@asynccontextmanager
async def lifespan(app):
    # Run startup logic
    create_db_and_tables()
    print("Database and tables created on startup.")
    yield
    # Run shutdown logic
    print("Cleanup or shutdown tasks can be placed here.")
