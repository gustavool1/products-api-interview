from flask import Blueprint

from app.controllers.products_controller import create_product, delete_product, get_all_products, update_product

bp = Blueprint("products", __name__)

bp.post("/products")(create_product)
bp.get("/products")(get_all_products)
bp.patch("/products/<int:id>")(update_product)
bp.delete("/products/<int:id>")(delete_product)