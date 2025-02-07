from git_exercise.users.user import User
from typing import Optional

class UsersGateway:
    users: list[User]
    
    def __init__(self):
        self.users = [
            User(id=1, name="Vishnu Vardhan", email="something@gmail.com", is_admin=True),
            User(id=2, name="Vishnu", email="something1@gmail.com", is_admin=False),
            User(id=3, name="Someone", email="something2@gmail.com", is_admin=False),
            User(id=4, name="Anyone", email="something3@gmail.com", is_admin=True),
        ]
    
    def find(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def list(self):
        return self.users
