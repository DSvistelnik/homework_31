import factory

from ads.models import Advertisement, Category
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    birth_date = "2000-01-01"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    slug = factory.Faker("ean", length=8)


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertisement

    name = factory.Faker("name")
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    price = 2000
    is_published = False
