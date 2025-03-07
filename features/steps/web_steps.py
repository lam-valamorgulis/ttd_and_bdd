@when('I request a list of products')
def step_impl(context):
    context.response = context.client.get("/products")
