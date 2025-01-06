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




# import jwt
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from src.models.user import User

# # Replace with your secret key
# SECRET_KEY = "your_secret_key"
# ALGORITHM = "HS256"  # Algorithm used to encode the token

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         # Decode the token
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
#         # Extract user information from the payload
#         user_id = payload.get("user_id")
#         username = payload.get("username")
        
#         if user_id is None or username is None:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Invalid token payload",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
        
#         # Create and return the user object
#         return User(id=user_id, username=username)
    
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Token has expired",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     except jwt.PyJWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
