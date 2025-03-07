@app.route("/products", methods=["GET"])
def list_products():
    return jsonify([product.serialize() for product in Product.all()]), 200

@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    product = Product.find(product_id)
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.find(product_id)
    data = request.get_json()
    product.update_from_dict(data)
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.find(product_id)
    product.delete()
    return '', 204
