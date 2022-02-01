from app.models.products_model import Products
from flask import request, jsonify
from http import HTTPStatus

def create_product():
    try:
        data = request.get_json()
        
        product = Products(**data)
        product.create_product()
        Products.serialize_product(product)

        return product.__dict__, HTTPStatus.CREATED
    except TypeError:
        return {"msg":"Missing required fields or given more than necessary"}, HTTPStatus.BAD_REQUEST

def get_all_products():
    all_products = Products.get_all_products()
    print(all_products)