from src.model.user import User
from src.repository.user_repository import UserRepository

from src.serializers.user_serializer import UserSerializer


class UserService:
    def __init__(self, user_repository: UserRepository, serializer: UserSerializer):
        self._user_repository = user_repository
        self._serializer = serializer

    def get_all_users(self):
        users = self._user_repository.get_all_users()
        serialized_users = [self._serializer.user_all_fields(user) for user in users]

        return serialized_users

    def get_user_by_email(self, email: str) -> User:
        return self._user_repository.get_user_by_email(email)

    def create_user(self, name: str, email: str, address: str) -> bool:
        new_user = User()
        new_user.name = name
        new_user.email = email
        new_user.address = address

        return self._user_repository.create_user(new_user)
