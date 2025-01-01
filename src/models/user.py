from pydantic import BaseModel

class User(BaseModel):
    id: str
    username: str
    # Add other user attributes here