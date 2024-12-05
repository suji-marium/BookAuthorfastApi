from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import date

class BookRequest(BaseModel):
    title: str = Field(index=True,min_length=1,max_length=200)
    published_date: date = Field(le=date.today())
    author_id: int

"""
    @model_validator(mode="before")
    def check_published_date(cls,values):
         published_date=values.get("published_date")
         if published_date and published_date>date.today():
             raise ValueError("Published date cannot be in the future.")
         return values

    @field_validator('title')
    @classmethod
    def title_must_not_be_empty(cls, v: str) -> str:
        if v.strip() == "":
            raise ValueError("Title cannot be empty")
        return v
"""
