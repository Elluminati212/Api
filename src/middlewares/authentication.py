import jwt
from fastapi import Depends, HTTPException, status, FastAPI
from fastapi.security import OAuth2PasswordBearer
from src.models.user import User
from pymongo import MongoClient
from bson.json_util import dumps, loads
import os

# Replace with your secret key
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"  # Algorithm used to encode the token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Extract user information from the payload
        user_id = payload.get("user_id")
        username = payload.get("username")
        
        if user_id is None or username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Create and return the user object
        return User(id=user_id, username=username)
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Protected route that requires a valid token
@app.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! You have access to this route."}
