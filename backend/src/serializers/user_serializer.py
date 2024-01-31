from src.model.user import User


class UserSerializer:

    def user_all_fields(self, user: User):
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address
        }
