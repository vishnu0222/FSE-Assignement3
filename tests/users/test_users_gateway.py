import unittest
from git_exercise.users.user import User
from git_exercise.users.users_gateway import UsersGateway

class TestUsersGateway(unittest.TestCase):
    def test_list(self):
        gateway = UsersGateway()
        result = [user.to_dict() for user in gateway.list()]
        
        expected_user = {
            "id": 1,
            "name": "Vishnu Vardhan",
            "email": "something@gmail.com",
            "is_admin": True
        }

        self.assertEqual(4, len(result))
        self.assertIn(expected_user, result)

    def test_find(self):
        gateway = UsersGateway()

        expected_user = {
            "id": 2,
            "name": "Vishnu",
            "email": "something1@gmail.com",
            "is_admin": False
        }

        self.assertEqual(gateway.find(2).to_dict(), expected_user)
        self.assertIsNone(gateway.find(1234))
