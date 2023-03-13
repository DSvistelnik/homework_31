import pytest
from rest_framework import status

from tests.factories import AdsFactory


@pytest.mark.django_db
def test_selections_create(client, user, access_token):

    ad_list = AdsFactory.create_batch(10)
    data = {
        "owner": user.pk,
        "items": [ad.pk for ad in ad_list],
        "name": "test"
    }

    expected_response = {
            "id": 1,
            "name": "test",
            "owner": user.pk,
            "items": [ad.pk for ad in ad_list]
        }

    response = client.post("/selection/create/", data=data, HTTP_AUTHORIZATION=f"Bearer {access_token}")

    # assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_response
