from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://<username>:<password>@",
    server_api=ServerApi('1')
)
db = client.book

db.cats.insert_many([{
                    "name": "barsik",
                     "age": 3,
                     "features": ["ходить в капці", "дає себе гладити", "рудий"]
                     },
                     {
                    "name": "Lama",
                    "age": 2,
                    "features": ["ходить в лоток", "не дає себе гладити", "сірий"]
},
    {
    "name": "Liza",
    "age": 4,
    "features": ["ходить в лоток", "дає себе гладити", "білий"]
}])
