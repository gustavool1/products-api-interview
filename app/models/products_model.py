import pymongo 
import os 
from datetime import datetime
from dotenv import load_dotenv



load_dotenv()

USER =  os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
client = pymongo.MongoClient(f"mongodb+srv://{USER}:{PASSWORD}@cluster0.yrtgs.mongodb.net/interview-test?retryWrites=true&w=majority")
DATABASE = os.getenv("DATABASE")
COLLECTION = os.getenv("COLLECTION")
print(len(DATABASE), '---TESTANDOOOOO')
print(len(COLLECTION), 'COLLLEEEECCCTION')
# client = pymongo.MongoClient(db=DATABASE, username=USER, password=PASSWORD, host="mongodb+srv://{USER}:{PASSWORD}@cluster0.yrtgs.mongodb.net/interview-test?retryWrites=true&w=majority")
db = client[DATABASE]
time_of_creation = str(datetime.now().strftime("%d/%m/%Y %H:%M"))

class Products():
    valid_keys = ["name", "image", "price"]

    def __init__(self,name,price, image='', created_at=time_of_creation, updated_at = None) -> None:
        self.name = name
        self.price = price 
        self.image = image
        self.created_at = created_at
        self.updated_at = updated_at
        self.id = self.generate_id()

    def __repr__(self) -> str:
        return f"Nome: {self.name} | Preço: {self.price} | Created: {self.created_at} | Updated : {self.updated_at}"


    def generate_id(self):
        if not len(list(db.get_collection(COLLECTION).find())):
            id = 1
        else:
            id = list(db.get_collection(COLLECTION).find())[-1]["id"] +1
        return id


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

    @staticmethod
    def delete_product(id):
        deleted_product = db.get_collection(COLLECTION).find_one_and_delete({"id":id})
        return deleted_product


    @classmethod
    def update_product(cls,id, data):
        updated_product = db.get_collection(COLLECTION).find_one_and_update({"id":id}, {"$set":data}, return_document=pymongo.ReturnDocument.AFTER)
        cls.serialize_product(updated_product)
        return updated_product
