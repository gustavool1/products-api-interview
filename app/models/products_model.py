import pymongo 
import os 
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
DATABASE = os.getenv("DATABASE")
COLLECTION = os.getenv("COLLECTION")
db = client[DATABASE]

time_of_creation = str(datetime.now().strftime("%d/%m/%Y %H:%M"))

class Products():
    def __init__(self,name,price, image='', created_at=time_of_creation, updated_at = None) -> None:
        self.name = name
        self.price = price 
        self.image = image
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return f"Nome: {self.name} | Preço: {self.price} | Created: {self.created_at} | Updated : {self.updated_at}"

    def create_product(self):
        db.get_collection(COLLECTION).insert_one(self.__dict__)


    @staticmethod
    def serialize_product(data):
        if type(data) is list:
            for post in data:
                post.update({"_id":str(post["_id"])})

        if type(data) is Products:
            data._id = str(data._id)

        if type(data) is dict:
            data.update({"_id":str(data["_id"])})
        
    @staticmethod
    def get_all_products():
        all_products = db.get_collection(COLLECTION).find()
        return all_products
