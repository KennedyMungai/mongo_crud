"""Script to hold password hashing logic"""
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    """Created a template for the HasPassword info"""

    def create_hash(self, password: str):
        """Function to create password hashes

        Args:
            password (str): The raw string password

        Returns:
            Hashed password: The password after being hashed
        """
        return pwd_context.hash(password)

    def verify_hash(self, plain_password: str, hashed_password: str):
        """A function to compare a normal text password to a hash password

        Args:
            plain_password (str): The plain text password
            hashed_password (str): The hashed password

        Returns:
            bool: Returns the state of comparison between the two password variables
        """
        return pwd_context.verify(plain_password, hashed_password)
