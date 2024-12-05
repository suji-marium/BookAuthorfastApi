from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import date

class BookRequest(BaseModel):
    title: str = Field(index=True,min_length=1,max_length=200)
    published_date: date = Field(le=date.today())
    author_id: int


