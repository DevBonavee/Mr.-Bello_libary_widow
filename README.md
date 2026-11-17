[README.md](https://github.com/user-attachments/files/34973422/README.md)
[README.md](https://github.com/user-attachments/files/34973515/README.md)
# Mr. Bello's Library Window

A Python command-line library management backend that processes text-based requests to manage books. The project demonstrates CRUD operations, user authentication, role-based permissions, persistent JSON storage, validation, error handling, and request logging.

## Features

- Authenticate authorised users with a username and password.
- Lock a user out after three failed login attempts.
- Support two roles: Member and Chief Librarian.
- List all books, retrieve a specific book, and list borrowed books.
- Add new books and update existing book details.
- Restrict book deletion to the Chief Librarian.
- Persist book records in `books.json`.
- Create an initial set of ten books when the data file does not exist.
- Detect and handle corrupted book data.
- Log each request with its timestamp, username, request text, and response code.

## CRUD operations

| Operation | Request | Purpose |
|---|---|---|
| Read all | `GET books` | Display all books |
| Read one | `GET book 4` | Display a specific book |
| Read borrowed | `GET books borrowed` | Display borrowed books |
| Create | `POST book` | Add a book |
| Update | `PUT book 4` | Update a book |
| Delete | `DELETE book 4` | Delete a book (Chief Librarian only) |

Each book contains an ID, title, author, and status. Status is either `on shelf` or `borrowed`.

## Roles and permissions

| Role | Permissions |
|---|---|
| Member | View, add, and update books |
| Chief Librarian | All Member permissions, plus delete books |

The application locks an account after three unsuccessful login attempts.

## Response codes

| Code | Meaning |
|---|---|
| `200` | Request completed successfully |
| `201` | A new book was created |
| `400` | Invalid request |
| `401` | User is not authenticated |
| `403` | User is authenticated but lacks permission |
| `404` | Requested book does not exist |

## Tech stack

- Python 3
- JSON file storage
- Python standard library

No third-party Python packages are required.

## Project structure

```text
Mr.-Bello_libary_widow/
├── library/
│   ├── __init__.py
│   ├── auth.py
│   ├── books.py
│   ├── logger.py
│   └── storage.py
├── books.json
├── main.py
└── README.md
```

## Getting started

```bash
git clone https://github.com/DevBonavee/Mr.-Bello_libary_widow.git
cd Mr.-Bello_libary_widow
python main.py
```

Sign in using one of the authorised accounts configured for the exercise. Do not reuse sample credentials in a real application.

## Example session

After signing in, enter a request such as:

```text
GET books
```

To add a book:

```text
POST book
```

The program prompts for the book's title, author, and status.

To update a book:

```text
PUT book 4
```

To delete a book:

```text
DELETE book 4
```

Only a Chief Librarian account can complete the delete operation. Enter `exit` to close the program.

## How the code is organised

- `main.py` — receives requests and displays responses.
- `auth.py` — handles login, failed attempts, account locking, and roles.
- `books.py` — implements book retrieval and CRUD operations.
- `storage.py` — loads and saves the JSON book ledger.
- `logger.py` — records requests and response codes.

## Learning outcomes

This project demonstrates separation of concerns, CRUD design, authentication, authorisation, file persistence, input validation, error handling, and audit-style logging.

## Author

Chukwuebuka Bonaventure — [@DevBonavee](https://github.com/DevBonavee)
