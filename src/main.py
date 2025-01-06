# from fastapi import FastAPI
# from src.routers import user_controller
# from fastapi.middleware.cors import CORSMiddleware
# from starlette.middleware.trustedhost import TrustedHostMiddleware
# from src.config import settings
# from pydantic_settings import BaseSettings
# from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from src.config.config import Settings
# from src.middlewares.auth import get_current_user
# from src.models.user import User

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.add_middleware(
#     TrustedHostMiddleware,
#     allowed_hosts=["*"],  # Replace with your actual domain(s)
# )

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # @app.get("/")
# # async def read_root():
# #     return {"message": "Hello World"}

# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     # Replace this with actual authentication logic
#     if form_data.username == "user" and form_data.password == "password":
#         return {"access_token": "valid_token", "token_type": "bearer"}
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

# app.include_router(user_controller.router, dependencies=[Depends(get_current_user)])

# #app.include_router(user_controller.router)


# def get_mongo_client():
#     try:
#         # Correctly create a MongoDB client
#         print(settings.db_url)
#         client = BaseSettings(settings.db_url)
#         return client
#     except Exception as e:
#         raise RuntimeError(f"Failed to connect to MongoDB: {e}")


# @app.get("/get_prediction")
# def get_prediction():
#     try:
#         # Connect to MongoDB
#         client = get_mongo_client()
#         print(settings.db_name)
#         print(client)
#         db = client[settings.db_name]  # Access the database using db_name
#         collection = db['prediction']  # Access the collection named 'prediction'

#         # Fetch all predictions from the database
#         predictions = list(collection.find({}, {"_id": 0, "latitude": 1, "longitude": 1, "cluster": 1, "trip_type": 1, "booking_type": 1, "ds": 1, "price_min": 1, "price_max": 1}))
#         print(predictions)  # Print the fetched predictions
#         return {"status": "success", "data": "predictions"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
        

# # Call the function to test
# if __name__ == "__main__":
#     all_predictions = get_prediction()
#     print("All Predictions:", all_predictions)


# if __name__ == "__main__":
#     import uvicorn
#     # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)






from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson.json_util import dumps, loads
import os

# Initialize FastAPI app
app = FastAPI()


@app.get("/test_connection")
async def test_connection():
    try:
        # Check MongoDB connection
        db.command("ping")
        return {"status": "Connection Successful"}
    except Exception as e:
        print(f"MongoDB connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")
    


# MongoDB connection
# MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://vpatel179:LqpC2zz4rO7pmtkR@cluster0.ejksq.mongodb.net/")  # Replace with your MongoDB URI
MONGO_URI = ("mongodb+srv://vpatel179:LqpC2zz4rO7pmtkR@cluster0.ejksq.mongodb.net/")  # Replace with your MongoDB URI
DB_NAME = "WriteDB"  # Replace with your database name

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["prediction"]
print(list(collection.find().limit(1)))  # Fetch one document to inspect

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["prediction"]
print(collection)
import math

# Helper function to sanitize float values
def sanitize_data(data):
    for record in data:
        for key, value in record.items():
            if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
                record[key] = None  # Replace invalid float with None
    return data

@app.get("/prediction")
async def get_prediction():
    try:
        # Fetch data from MongoDB
        prediction = list(collection.find({}, {
            "_id": 0,
            "latitude": 1,
            "longitude": 1,
            "cluster": 1,
            "trip_type": 1,
            "booking_type": 1,
            "ds": 1,
            "price_min": 1,
            "price_max": 1
        }))
        
        # Sanitize data for JSON compliance
        sanitized_prediction = sanitize_data(prediction)
        return sanitized_prediction
    except Exception as e:
        # Log and raise HTTP exception
        print(f"Error fetching predictions: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
