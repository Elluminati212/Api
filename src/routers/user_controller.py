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

'''
# filepath: /home/vasu/app/src/main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pymongo import MongoClient

app = FastAPI()

def get_mongo_client():
    """
    Connect to MongoDB.
    Replace the connection string with your actual database credentials.
    """
    client = MongoClient("mongodb+srv://vpatel179:LqpC2zz4rO7pmtkR@cluster0.ejksq.mongodb.net/")
    return client

@app.get('/')
async def get_prediction():
    try:
        # Connect to MongoDB
        client = get_mongo_client()
        db = client['WriteDB'] # Replace with your database name
        collection = db['prediction'] # Replace with your collection name
        
        # Fetch all predictions from the database
        predictions = list(collection.find({}, {"_id": 0, "latitude": 1, "longitude": 1, "cluster": 1, "trip_type": 1, "booking_type": 1, "ds": 1, "price_min": 1, "price_max": 1})) # Exclude MongoDB _id field
        if not predictions:
            return JSONResponse(status_code=404, content={"status": "error", "message": "No data found in the collection."})
        
        return JSONResponse(status_code=200, content={
            "status": "success",
            "data": predictions
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
'''



