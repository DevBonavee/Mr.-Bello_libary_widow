from library.storage import load_books, save_books


def get_all_books():
    books = load_books()
    return 200, books

def get_one_book(book_id):
    books = load_books()

    for book in books:
        if book["book_id"] == book_id:
            return 200, book


    return 404, "There is no such book."

def get_borrowed_books():
    books = load_books()

    borrowed_books = []

    for book in books:
        if book["status"] == "borrowed":
            borrowed_books.append(book)

    return 200, "There is no such book."   


def add_book(title, author, status):
    books = load_books()

    if not title or not author or not status:
        return 400, "I cannot read this slip."

    if status not in ["on shelf", "borrowed"]:
        return 400, "I cannot read this slip."

    new_book_number = 1

    if books:
        new_book_number = max(book["book_id"] for book in books) + 1

    new_book = {
        "book_1d": new_book_number,
        "title": title,
        "author": author,
        "status": status
    } 

    books.append(new_book)
    save_books(books)

    return 201, new_book

def update_book(book_id, title, author, status):
    books = load_books()

    if not title or not author or not status:
        return 400, "I cannot read this slip." 

    if status not in ["on shelf", "borrowed"]:
        return 400, "I cannot read this slip."

    for book in books:
        if book["book_id"] == book_id:
            book["title"] = title
            book["author"] = author
            book["status"] = status

            save_books(books)

            return 200, book

    return 404, "There is no such book."

def delete_book(book_id):
     books = load_books()

     for book in books:
         if book["book_id"] == book_id:
             books.remove(book)
             save_books(books)


             return 200, "Book removed successfully."   

     return 404, "There is no such book."    