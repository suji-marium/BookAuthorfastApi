from pydantic import BaseModel

from app.models.book import Book

class AuthorResponse(BaseModel):
    id: int
    name: str
    books: list[Book]
