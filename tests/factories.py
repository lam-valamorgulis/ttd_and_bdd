import factory
from factory.fuzzy import FuzzyChoice
from service.models import Product  # Ensure you have your Product model imported

class ProductFactory(factory.Factory):
    """Generates fake Product instances for testing"""
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    category = FuzzyChoice(["Electronics", "Clothing", "Home", "Toys"])
    price = factory.Faker("random_number", digits=2)
    available = FuzzyChoice([True, False])
