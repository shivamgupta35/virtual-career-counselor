import json
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = "data/users.json"

def load_users():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DB_PATH, "w") as f:
        json.dump(users, f, indent=4)

def create_user(name, email, password):
    users = load_users()

    # prevent duplicate email
    for u in users:
        if u["email"] == email:
            return None

    user = {
        "id": str(uuid.uuid4()),
        "name": name,
        "email": email,
        "password": generate_password_hash(password)
    }

    users.append(user)
    save_users(users)
    return user

def authenticate_user(email, password):
    users = load_users()
    for user in users:
        if user["email"] == email and check_password_hash(user["password"], password):
            return user
    return None
