from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Encryption():
    def encrypt(password: str):
        return pwd_context.hash(password)