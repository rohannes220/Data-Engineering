import pymongo
import json
from bson import json_util
import os

# --- Setup relative paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'catalog.json')

# --- Connect to MongoDB ---
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["catalog"]

# --- Task 1: Import 'catalog.json' into MongoDB ---
with open(DATA_PATH) as file:
    for line in file:
        data = json.loads(line, object_hook=json_util.object_hook)
        db.electronics.insert_one(data)
print("Task 1: Imported 'catalog.json' into MongoDB")

# --- Task 2: List all databases ---
databases = client.list_database_names()
print("\nTask 2: Databases:")
print(databases)

# --- Task 3: List all collections in 'catalog' ---
collections = db.list_collection_names()
print("\nTask 3: Collections in 'catalog' database:")
print(collections)

# --- Task 4: Create an index on 'type' field ---
index_name = db.electronics.create_index("type")
print("\nTask 4: Created index on 'type' field:")
print(index_name)

# --- Task 5: Count number of laptops ---
laptop_count = db.electronics.count_documents({"type": "laptop"})
print("\nTask 5: Number of laptops:", laptop_count)

# --- Task 6: Count smartphones with screen size 6 inches ---
smartphone_6inch_count = db.electronics.count_documents({"type": "smart phone", "screen size": 6})
print("\nTask 6: Number of smartphones with a screen size of 6 inches:", smartphone_6inch_count)

# --- Task 7: Average screen size of smartphones ---
pipeline = [
    {"$match": {"type": "smart phone"}},
    {"$group": {"_id": None, "average_screen_size": {"$avg": "$screen size"}}}
]
average_screen_size = list(db.electronics.aggregate(pipeline))[0]["average_screen_size"]
print("\nTask 7: Average screen size of smartphones:", average_screen_size)

