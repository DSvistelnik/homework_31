from pytest_factoryboy import register

from tests.factories import AdsFactory, UserFactory, CategoryFactory

pytest_plugins = "tests.fixtures"

register(UserFactory)
register(CategoryFactory)
register(AdsFactory)
