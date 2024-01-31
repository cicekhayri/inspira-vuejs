from inspira.decorators.http_methods import get, post
from inspira.decorators.path import path
from inspira.responses import JsonResponse
from inspira.requests import Request

from src.service.user_service import UserService


@path("/users")
class UserController:
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    @get()
    async def index(self, request: Request):
        users = self._user_service.get_all_users()

        context = {
            "users": users
        }

        return JsonResponse(context)

    @post()
    async def create_user(self, request: Request):
        body = await request.json()
        name = body["name"]
        email = body["email"]
        address = body["address"]

        self._user_service.create_user(name, email, address)
        return JsonResponse({"message": "Successful"})
