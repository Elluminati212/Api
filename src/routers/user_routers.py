# filepath: /home/vasu/app/routers/user_router.py
from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/users")
async def read_users():
    return [{"username": "user1"}, {"username": "user2"}]