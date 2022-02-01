from flask import Blueprint

from app.controllers.products_model import create_product, get_all_products

bp = Blueprint("products", __name__)

bp.post("/products")(create_product)
bp.get("/products")(get_all_products)