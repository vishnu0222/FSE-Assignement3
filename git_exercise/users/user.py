from dataclasses import dataclass

class User:
    def __init__(self, id: int, name: str, email: str, is_admin: bool = False):
        self.id = id
        self.name = name
        self.email = email
        self.is_admin = is_admin

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "is_admin": self.is_admin
        }
