
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

    # @model_validator(mode="before")
    # def check_published_date(cls,values):
    #     published_date=values.get("published_date")
    #     if published_date and published_date>date.today():
    #         raise ValueError("Published date cannot be in the future.")
    #     return values

    @field_validator('title')
    @classmethod
    def title_must_not_be_empty(cls,v: str) -> str:
        if v.strip() == "":
            raise ValueError("Title cannot be empty")
        return v
