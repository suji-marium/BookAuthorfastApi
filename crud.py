from pydantic import ValidationError
from sqlmodel import Session,select

from app.exceptions.exceptions import AuthorHasBooksException
from app.models.author import Author
from app.models.book import Book
from fastapi import HTTPException

def create_author(author:Author,session:Session)->Author:
    try:
        #author.__validate__()
        session.add(author)
        session.commit()
        session.refresh(author)
        return author

    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))


def create_book(book:Book,session:Session)->Book:
    try:
        author=session.get(Author,book.author_id)
        if not author:
            raise HTTPException(status_code=404,detail="Author id not found")
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

    except ValidationError as e:
        raise HTTPException(status_code=400,detail=str(e))

def get_authors(session:Session) -> list[Author]:
    return session.exec(select(Author)).all()

def get_books(session:Session)->list[Book]:
    return session.exec(select(Book)).all()

def get_author(author_id:int,session:Session)->Author:
    return session.get(Author,author_id)

def get_book(book_id:int,session:Session)->Book:
    return session.get(Book,book_id)

def delete_book(book_id:int,session:Session)->Book:
    book=session.get(Book,book_id)
    if not book:
        return None
    session.delete(book)
    session.commit()
    return book

def delete_author(author_id:int,session:Session)->Author:
    author=session.get(Author,author_id)
    if not author:
        raise HTTPException(status_code=404,detail="Author not found")


    books=session.exec(select(Book).where(Book.author_id == author_id)).all()
    if books:
        raise AuthorHasBooksException(author_id)

    session.delete(author)
    session.commit()
    return author

"""
 author = session.exec(select(Author).where(Author.id == author_id)).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    # Check if the author has any books associated with them
    books = session.exec(select(Book).where(Book.author_id == author_id)).all()
    if books:
        raise AuthorHasBooksException(author_id)
    
    # Delete the author if no books exist
    session.delete(author)
    session.commit()
"""
