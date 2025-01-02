from fastapi import FastAPI
# from routers.user_controller from routers
# from routers import user_controller
from src.routers import user_controller
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from pydantic_settings import BaseSettings


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],  # Replace with your actual domain(s)
)

app.include_router(user_controller.router) 

def get_mongo_client():

    client = BaseSettings.db_url
    return client

@app.route('/', methods=['GET'])
def get_prediction():
    try:
        # Connect to MongoDB
        client = get_mongo_client()
        db = client['WriteDB'] # Replace with your database name
        collection = db['prediction'] # Replace with your collection name

        # Fetch all predictions from the database
        predictions = list(collection.find({}, {"_id": 0, "latitude": 1, "longitude": 1, "cluster": 1, "trip_type": 1, "booking_type": 1, "ds": 1, "price_min": 1, "price_max": 1})) # Exclude MongoDB _id field
        print(db.prediction.find())
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
