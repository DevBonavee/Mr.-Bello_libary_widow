from library.auth import login_user
from library.books import (
    get_all_books,
    get_one_book,
    get_borrowed_books,
    add_book,
    update_book,
    delete_book
)
from library.logger import record_request
from library.storage import LedgerError

def show_books(books):
    for book in books:
        print(
             f"{book['book_id']}. "
            f"{book['title']} - "
            f"{book['author']} - "
            f"{book['status']}"
        )

def handle_request(current_user, request):
    parts = request.split()

    if not parts:
        return 400, "I cannot read this slip."

    action = parts[0].upper()

    if action not in ["GET", "POST", "PUT", "DELETE"]:
        return 400, "I Cannot read this slip."

    if action == "Get":
        if len(parts) == 2 and parts[1].lower() == "books":
            code, result = get_all_books()

            if code == 200:
                show_books(result)

            return code, "done, here you are."

        if (
             len(parts) == 3
            and parts[1].lower() == "books"
            and parts[2].lower() == "borrowed"
        ): 

            code, result = get_all_books()

            if code == 200:
                show_books(result)

            return code, "Done, here you are."

        if len(parts) == 3 and parts[1].lower() == "book":

            try:
                book_id = int(parts[2]) 
            except ValueError:
                return 400, "I cannot read this slip."

            code, result = get_one_book(book_id)  

            if code == 200:
                show_books([result])
                return code, "Done, here you are."

            return code, result

        return 400, "I cannot read this slip." 

    if action == "POST":
        if len(parts) != 2or parts[1].lower() != "book":     
            return 400, "I cannot read this slip."

        print("\nEnter the new book details.")

        title = input("Title: ").strip()
        author = input("Author: ").strip()
        status = input("Status (on shelf/borrowed): ").strip().lower()

        return add_book(title, author, status)  


    if action == "PUT":
        if len(parts) != 3 or parts[1].lower() != "book":
            return 400, "I cannot read this Slip."

        try:
            book_id = int(parts[2])
        except ValueError:
            return 400, "I cannot read this slip."

        title = input("New title: ").strip()
        author = input("New author: ").strip()
        status = input("New status (on shelf/borrowed): ").strip().lower()

        return update_book(book_id, title, author, status)

    if action == "DELETE":
        if len(parts) != 3 or parts[1].lower () != "book":
            return 400, "I cannot read this slip."

        if current_user["position"] != "Chief librarian":
            return 403, "I know who you are, and you are not allowed to do this."

        try:
           book_id = int(parts[2])
        except ValueError:
            return 400, "I cannot read this slip."

        return delete_book(book_id)


def start_library():
    print("================================")
    print("      MR. BELLO'S LIBRARY")
    print("================================")

    current_user = None

    while current_user is None:
        username = input("\nUsername: ").strip()
        password = input("Password: ").strip()

        user, message = login_user(username, password)

        print(message)

        if user is not None:
            current_user = user

    print(f"\nWelcome, {current_user['username']}.")
    print("Type 'exit' to close the library.")


    while True:
        request = input("\nLibrary window > ").strip()

        if request.lower() == "exit":
            print("Goodbye.")
            break

        try:
            code, message = handle_request(current_user, request)

            print(f"{code} {message}")

            record_request(
                current_user["username"],
                request,
                code
            )

        except LedgerError as error:
            print(f"400 {error}")

            record_request(
                current_user["username"],
                request,
                400
            )


        except Exception:
            print("400 I cannot read this slip.")

            record_request(
                current_user["username"],
                request,
                400
            )


if __name__ == "__main__":
    start_library()


            



