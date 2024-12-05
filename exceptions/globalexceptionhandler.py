from fastapi.responses import JSONResponse
from fastapi import Request

from app.exceptions.exceptions import AuthorHasBooksException


# Global exception handler for AuthorHasBooksException
def setup_exception_handlers(app):
    @app.exception_handler(AuthorHasBooksException)
    async def author_has_books_exception_handler(request, exc: AuthorHasBooksException):
        return JSONResponse(
            status_code=400,
            content={"message": f"Cannot delete author {exc.author_id} because they have associated books."},
        )
