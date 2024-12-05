from fastapi import FastAPI,HTTPException
from fastapi.params import Depends

from app.crud import create_author, create_book, get_authors, get_books, get_author, get_book, delete_book, \
    delete_author
from app.exceptions.globalexceptionhandler import setup_exception_handlers
from app.models.author import Author
from app.dependency import get_session
from app.database import lifespan

from sqlmodel import Session

from app.models.authorRequest import AuthorRequest
from app.models.book import Book
from app.models.authorResponse import AuthorResponse
from app.models.bookRequest import BookRequest
from app.models.bookResponse import BookResponse

app=FastAPI(lifespan=lifespan)
setup_exception_handlers(app)


@app.post("/author")
def create_author_route(author:AuthorRequest,session:Session=Depends(get_session))->Author:
    author_data=Author(**author.model_dump())
    return create_author(author_data,session)

@app.post("/book")
def create_book_route(book:BookRequest,session:Session=Depends(get_session))->Book:
    book_data = Book(**book.model_dump())
    return create_book(book_data,session)

@app.get("/authors",response_model=list[AuthorResponse])
def get_authors_route(session:Session=Depends(get_session))->list[Author]:
    return get_authors(session)

@app.get("/books",response_model=list[BookResponse])
def get_books_route(session:Session=Depends(get_session))->list[Book]:
    return get_books(session)

@app.get("/author/{author_id}")
def get_author_route(author_id:int,session:Session=Depends(get_session))->Author:
    author= get_author(author_id,session)
    if not author:
        raise HTTPException(status_code=404,detail="Author not found")
    return author

@app.get("/book/{book_id}")
def get_book_route(book_id:int,session:Session=Depends(get_session))->Book:
    book=get_book(book_id,session)
    if not book:
        raise HTTPException(status_code=404,detail="Book not found")
    return book

@app.delete("/book/{book_id}")
def delete_book_route(book_id:int,session:Session=Depends(get_session))->Book:
    book=delete_book(book_id,session)
    if not book:
        raise HTTPException(status_code=404,detail="Book not found")
    return book

@app.delete("/author/{author_id}")
def delete_author_route(author_id:int,session:Session=Depends(get_session))->Author:
    author=delete_author(author_id, session)
    return author

