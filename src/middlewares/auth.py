from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Logic to verify the token and retrieve user information from MongoDB goes here
    # If token is valid, return the User object
    # If token is invalid, raise an HTTPException
    if token == "valid_token": # Replace with actual token verification logic
        return User(id="123", username="testuser")
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
