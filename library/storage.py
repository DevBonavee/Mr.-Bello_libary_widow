import json 
import os


BOOKS_FILE = "books.json"

class LedgerError(Exception):
    pass


def get_initial_books():
    books = [
       {
            "book_id": 1,
            "title": "Things Fall Apart",
            "author": "Chinua Achebe",
            "status": "on shelf"
        },
        {
            "book_id": 2,
            "title": "Purple Hibiscus",
            "author": "Chimamanda Adichie",
            "status": "borrowed"
        },
        {
            "book_id": 3,
            "title": "The Famished Road",
            "author": "Ben Okri",
            "status": "on shelf"
        },
        {
            "book_id": 4,
            "title": "Sozaboy",
            "author": "Ken Saro-Wiwa",
            "status": "on shelf"
        },
        {
            "book_id": 5,
            "title": "Jagua Nana",
            "author": "Cyprian Ekwensi",
            "status": "borrowed"
        },
        {
            "book_id": 6,
            "title": "The Joys of Motherhood",
            "author": "Buchi Emecheta",
            "status": "on shelf"
        },
        {
            "book_id": 7,
            "title": "Arrow of God",
            "author": "Chinua Achebe",
            "status": "on shelf"
        },
        {
            "book_id": 8,
            "title": "Stay With Me",
            "author": "Ayobami Adebayo",
            "status": "borrowed"
        },
        {
            "book_id": 9,
            "title": "The Fishermen",
            "author": "Chigozie Obioma",
            "status": "on shelf"
        },
        {
            "book_id": 10,
            "title": "Half of a Yellow Sun",
            "author": "Chimamanda Adichie",
            "status": "on shelf"
        }
    ]

    return books

def load_books():
    if not os.path.exists(BOOKS_FILE):
        books = get_initial_books()
        save_books(books)
        return books

    try:

        with open(BOOKS_FILE, "r") as file:
            books = json.load(file)

        if not isinstance(books, list):
            raise LedgerError("The saved ledger is corrupted.")    

        return books

    except(json.JSONDecodeError, OSError):
        raise LedgerError ("The saved Ledger is corrupted.")


def save_books(books):
    try:
        with open(BOOKS_FILE, "w") as file:
            json.dump(books, file, indent=4)


    except OSError:
        raise LedgerError("The ledger could not be saved.")
    