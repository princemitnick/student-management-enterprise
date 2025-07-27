import hashlib

from fastapi.security import OAuth2PasswordRequestForm

def get_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
