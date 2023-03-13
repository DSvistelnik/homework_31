import pytest
from rest_framework.status import HTTP_201_CREATED


@pytest.mark.django_db
def test_ad_create(client, user, category, access_token):
    data = {
        "author": user.username,
        "category": category.name,
        "name": "Сибирская котята, 3 месяца",
        "price": 2500,
        "is_published": False
    }

    expected_data = {
            "id": 24,
            "author": user.username,
            "category": category.name,
            "locations": [],
            "name": "Сибирская котята, 3 месяца",
            "price": 2500,
            "description": None,
            "is_published": False
        }

    response = client.post("/ad/", data=data, HTTP_AUTHORIZATION=f"Bearer {access_token}")

    response.status_code == HTTP_201_CREATED
    response.data = expected_data
