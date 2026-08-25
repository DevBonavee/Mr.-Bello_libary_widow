users = {
    "mrs_okafor": {
        "password": "library2024",
        "position": "Chief Librarian"
    },
    "bello_jr": {
        "password": "windowboy",
        "position": "Member"
    },
    "amina_s": {
        "password": "books4life",
        "position": "Member"
    },
    "tunde_reads": {
        "password": "password123",
        "position": "Member"
    },
    "chichi_o": {
        "password": "novels!",
        "position": "Member"
    },
    "baba_musa": {
        "password": "retired55",
        "position": "Member"
    }
}

wrong_attempts = {}
locked_users = set()


def login_user(username, password):
    if username in locked_users:
        return None, "401 Your sign-in has been locked."

    if username not in users:
        return None, "401 Who are you? Sign in first."

    if username not in wrong_attempts:
        wrong_attempts[username] = 0

    if password != users[username]["password"]:
        wrong_attempts[username] += 1

        if wrong_attempts[username] >= 3:
            locked_users.add(username)
            return None, "401 Three wrong attempts. The grille is closed."

        return None, "401 Who are you? Sign in first."

    wrong_attempts[username] = 0

    user = {
        "username": username,
        "position": users[username]["position"]
    }

    return user, "200 signed in successfully."