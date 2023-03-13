import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test"
    password = "test"
    django_user_model.objects.create_user(username=username, password=password, birth_date="2000-01-01", role="admin")

    response = client.post("/token/", {"username": username, "password": password})
    return response.data.get("access")
