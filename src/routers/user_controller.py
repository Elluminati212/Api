from fastapi import APIRouter, Depends
from src.middlewares.auth import get_current_user
from src.models import user
from src.models.user import User

router = APIRouter() 

@router.get("/")
async def get_users(current_user: User = Depends(get_current_user)):
    # Logic to fetch all users from MongoDB goes here
    # Use MongoDB driver to query the collection
    # Return a list of User objects
    return {"users": user}

@router.get("/{user_id}")
async def get_user(user_id: str, current_user: User = Depends(get_current_user)):
    # Logic to fetch a single user by ID from MongoDB goes here
    # Use MongoDB driver to query the collection
    # Return a User object
    return {"user": user}

@router.post("/")
async def create_user(user: User):
    # Logic to create a new user in MongoDB goes here
    # Use MongoDB driver to insert the user data
    # Return the created user
    return {"user": user}

@router.put("/{user_id}")
async def update_user(user_id: str, user: User):
    # Logic to update an existing user in MongoDB goes here
    # Use MongoDB driver to update the user data
    # Return the updated user
    return {"user": user}

@router.delete("/{user_id}")
async def delete_user(user_id: str):
    # Logic to delete a user from MongoDB goes here
    # Use MongoDB driver to delete the user data
    # Return a success message
    return {"message": "User deleted successfully"}

# @router.get("/users")
# async def read_users(current_user: User = Depends(get_current_user)):
#     return [{"username": "user1"}, {"username": "user2"}]