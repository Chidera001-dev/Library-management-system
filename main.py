import json
from models.book import Book
from models.library import Library
from models.users import Member
from services.library_service import LibraryService


def main():
    library = Library("My local Library")
    library_service = LibraryService(library)

    #Add book
    books_Lists = []
    with open("./data/books.json", "r") as file:
        books_Lists = json.load(file)

    for book in books_Lists:
        library.add_book(book=Book(book["title"], book["author"], book["isbn"]))


    user = Member("Chidera")
    user2 = Member("Alex")
    library.register_user(user)

    try:
        library_service.checkout_book(user,"To Kill a Mockingbird" )
        library_service.checkout_book(user,"1984" )
        print()
        for book in user.borrowed_books:
            print(book)
    except Exception as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    main()