from pymongo import MongoClient
from .config import settings

mongo_client = MongoClient(settings.db_url)