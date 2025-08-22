from uuid import uuid4


class Book:
    def __init__(
        self,
        book_id: str,
        isbn: str,
        title: str,
        author: str,
        publisher: str,
        year: int,
        genre: str,
        copies: int,
        available: int ,
        status: str,
    ) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.copies = copies
        self.available = available
        self.status = status

    def __repr__(self):
        return f"id: {self.book_id} | title: {self.title} | author: {self.author} | available: {self.available}"
           # f"publisher: {self.publisher} | year: {self.year} | genre: {self.genre} | "
            #f"available: {self.available}"

        
    