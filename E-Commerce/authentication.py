from passlib.context import CryptContext
from typing_extensions import deprecated

password_context = CryptContext(schemes=['bcrypt'])

def get_hashed_password(password):
    return password_context.hash(password)