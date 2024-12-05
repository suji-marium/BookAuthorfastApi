from pydantic import BaseModel
from datetime import date

from app.models.author import Author

class BookResponse(BaseModel):
    id: int
    title: str
    published_date: date
    author: Author