from app.exceptions.InvalidIdError import InvalidIdError
from app.exceptions.UpdatedInvalidBodyError import UpdatedInvalidBodyError
from app.models.products_model import Products
from flask import request, jsonify
from http import HTTPStatus
from datetime import datetime
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
    all_products = list(Products.get_all_products())
    Products.serialize_product(all_products)
    return jsonify(all_products), HTTPStatus.OK


def update_product(id):
    try:
        data = request.get_json()
        keys_of_data = data.keys()
        for key in keys_of_data: 
            if key not in Products.valid_keys:
                raise UpdatedInvalidBodyError 
        
        time_of_update = str(datetime.now().strftime("%d/%m/%Y %H:%M"))
        data.update({"updated_at":time_of_update})
        updated_product = Products.update_product(id, data)

        if not updated_product:
            raise InvalidIdError

        return updated_product, HTTPStatus.OK

    except UpdatedInvalidBodyError:
        return {"error":"This field cant be updated or doenst exist."}, HTTPStatus.BAD_REQUEST

    except InvalidIdError:
        return {"msg":"Invalid id"}, HTTPStatus.NOT_FOUND

def delete_product(id):
    print(id)
    return 'a'