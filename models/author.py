
from sqlmodel import SQLModel,Field,Relationship
from pydantic import model_validator


class Author(SQLModel,table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True,min_length=1,max_length=100)

    books:list["Book"]=Relationship(back_populates="author")

    @model_validator(mode="before")
    def check_name_not_empty(cls,values):
        name=values.get("name")
        print(name)
        if not name:
            raise ValueError("Name cannot be empty")
        return values
