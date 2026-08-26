from datetime import datetime


LOG_FILE = "library.log"


def record_request(username, request, response_code):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"{current_time} | "
        f"{username} | "
        f"{request} | "
        f"{response_code}\n"
    )

    with open(LOG_FILE, "a") as file:
        file.write(log_entry)