from pydantic import BaseModel, Field


class AuthorRequest(BaseModel):
    name: str = Field(index=True, min_length=1, max_length=100)

