from pydantic import BaseModel

class User(BaseModel):
    Id: str
    User: str
    # Add other user attributes here