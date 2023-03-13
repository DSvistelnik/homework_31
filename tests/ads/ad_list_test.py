import pytest
from rest_framework.status import HTTP_200_OK

from ads.serializers import AdSerializer
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_ads_list(client):
    ads = AdsFactory.create_batch(5)
    response = client.get("/ad/")

    expected_response = {"count": 5,
                         "next": None,
                         "previous": None,
                         "results": AdSerializer(ads, many=True).data
                         }

    assert response.status_code == HTTP_200_OK
    assert response.data == expected_response
