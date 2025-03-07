def test_read_product(client):
    product = ProductFactory()
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200

def test_update_product(client):
    product = ProductFactory()
    updated_data = {"name": "Updated Laptop"}
    response = client.put(f"/products/{product.id}", json=updated_data)
    assert response.status_code == 200

def test_delete_product(client):
    product = ProductFactory()
    response = client.delete(f"/products/{product.id}")
    assert response.status_code == 204

def test_list_all_products(client):
    ProductFactory.create_batch(3)
    response = client.get("/products")
    assert len(response.json) == 3

def test_list_by_name(client):
    ProductFactory(name="Laptop")
    response = client.get("/products?name=Laptop")
    assert response.status_code == 200

def test_list_by_category(client):
    ProductFactory(category="Electronics")
    response = client.get("/products?category=Electronics")
    assert response.status_code == 200

def test_list_by_availability(client):
    ProductFactory(available=True)
    response = client.get("/products?available=true")
    assert response.status_code == 200
