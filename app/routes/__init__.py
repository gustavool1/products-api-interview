from app.routes.products_routes import bp as bp_products
def init_app(app):
    app.register_blueprint(bp_products)