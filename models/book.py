
from pydantic import model_validator, field_validator, BaseModel
from sqlalchemy import false
from sqlmodel import SQLModel,Field, Relationship
from datetime import date

from app.models.author import Author


class Book(SQLModel,table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True,min_length=1)
    published_date: date = Field(lt=date.today())
    author_id:int=Field(foreign_key="author.id")

    author: Author | None =Relationship(back_populates="books")
