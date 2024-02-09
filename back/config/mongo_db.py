
from pymongo import MongoClient
from config.config import settings

client = MongoClient(settings.DATABASE_URL)
db = client['portfolio']
collection_user = db['usuario']


try:
    conn = client.server_info()
    print(f'Connected to MongoDB {conn.get("version")}')
except Exception:
    print("Unable to connect to the MongoDB server.")
