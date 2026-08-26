# Mr. Bello's Library Window

A simple Python backend for managing a library through a command-line interface.

## Overview

Mr. Bello's Library Window is a backend assignment built around a simple idea: users send requests through a library window, and the system processes each request and returns a response code.

The project implements the four basic CRUD operations:

* `GET` to view books
* `POST` to add a new book
* `PUT` to update an existing book
* `DELETE` to remove a book

It also includes user authentication, role-based permissions, persistent storage, input validation, error handling, and request logging.

## Features

### Authentication

The system has six authorised users. Each user signs in with a username and password.

There are two user roles:

* **Member**: Can view, add, and update books
* **Chief Librarian**: Has all member permissions and can also delete books

Users are locked out after three failed login attempts.

### Book Management

The system supports:

```text
GET books
GET book 4
GET books borrowed

POST book
PUT book 4
DELETE book 4
```

Each book contains:

* Book ID
* Title
* Author
* Status

A book can have either `on shelf` or `borrowed` as its status.

### Response Codes

Every request returns a response code.

| Code  | Meaning                                  |
| ----- | ---------------------------------------- |
| `200` | Request completed successfully           |
| `201` | New book created                         |
| `400` | Invalid request                          |
| `401` | User is not authenticated                |
| `403` | User is authenticated but not authorised |
| `404` | Requested book does not exist            |

### Persistent Storage

Books are stored in `books.json`.

The program creates the initial ten books automatically when the ledger does not exist. Changes made to the books are saved back to the file, so the data remains available after the program is closed and started again.

The program also checks for a corrupted ledger and handles the problem without exposing a Python traceback to the user.

### Request Logging

Requests are recorded in `library.log`.

Each log entry contains:

* Date and time
* Username
* Request
* Response code

## Project Structure

```text
mr-bellos-library/
│
├── main.py
├── books.json
├── library.log
│
└── library/
    ├── __init__.py
    ├── auth.py
    ├── books.py
    ├── logger.py
    └── storage.py
```

### `main.py`

Acts as the library window. It receives user requests, sends them to the appropriate function, and displays the response.

### `auth.py`

Handles the staff register, login verification, failed login attempts, account locking, and user roles.

### `books.py`

Contains the actual book operations. This is where books are retrieved, added, updated, and deleted.

### `storage.py`

Handles the library ledger. It creates the initial data, loads books from `books.json`, saves changes, and detects corrupted storage.

### `logger.py`

Records requests and their response codes in `library.log`.

### `__init__.py`

Marks the `library` directory as a Python package.

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Run the application

Make sure Python is installed, then run:

```bash
python main.py
```

### 3. Sign in

Use any of the authorised accounts:

| Username      | Password      | Role            |
| ------------- | ------------- | --------------- |
| `mrs_okafor`  | `library2024` | Chief Librarian |
| `bello_jr`    | `windowboy`   | Member          |
| `amina_s`     | `books4life`  | Member          |
| `tunde_reads` | `password123` | Member          |
| `chichi_o`    | `novels!`     | Member          |
| `baba_musa`   | `retired55`   | Member          |

## Example Requests

After signing in, you can use:

```text
GET books
```

to display all books.

```text
GET book 4
```

to display a specific book.

```text
GET books borrowed
```

to display only borrowed books.

To add a book:

```text
POST book
```

The program will ask for the title, author, and status.

To update a book:

```text
PUT book 4
```

The program will ask for the updated details.

To delete a book:

```text
DELETE book 4
```

Only the Chief Librarian can perform this operation.

Type:

```text
exit
```

to close the program.

## Design Approach

The project uses a simple separation of responsibilities.

`main.py` handles interaction with the user. Authentication is handled by `auth.py`, book operations are handled by `books.py`, file operations are handled by `storage.py`, and logging is handled by `logger.py`.

This keeps the project easier to understand, test, and maintain. It also means changes to one part of the application do not require putting unrelated logic into a single file.

## Testing

The application can be tested against the main requirements of the assignment:

```text
GET books              → 200
GET existing book      → 200
GET missing book       → 404
Invalid request        → 400
Unauthenticated user   → 401
Member DELETE          → 403
Chief Librarian DELETE → 200
New book               → 201
```

The storage system can also be tested by adding a book, closing the program, starting it again, and checking that the book is still present.

## Requirements

* Python 3
* No external Python packages are required

## Author
Chukwuebuka Bonaventure
Built as a backend development assignment focused on CRUD operations, authentication, authorisation, persistence, and clean project structure
