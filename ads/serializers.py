from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from ads.models import Advertisement, Category, Selection
from users.models import User

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class AdSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field="name")
    locations = SerializerMethodField()

    def get_locations(self, ad):
        return [location.name for location in ad.author.locations.all()]

    class Meta:
        model = Advertisement
        exclude = ["image"]


class AdDetailSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field="name")

    class Meta:
        model = Advertisement
        exclude = ["image"]


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdDetailSerializer(many=True)

    class Meta:
        model = Selection
        fields = ["id", "items", "name", "owner"]


class SelectionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id"]
