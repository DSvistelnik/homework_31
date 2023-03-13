import pytest
from rest_framework.status import HTTP_200_OK

from ads.serializers import AdSerializer
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_detail_ad(client, access_token):
    ad = AdsFactory.create()
    response = client.get(f"/ad/{ad.pk}/", HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == HTTP_200_OK
    assert response.data == AdSerializer(ad).data
