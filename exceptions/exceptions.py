
class AuthorHasBooksException(Exception):
    def __init__(self, author_id: int):
        self.author_id = author_id
