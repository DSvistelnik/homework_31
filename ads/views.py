import json
from typing import Type

from ads.models import Category, Advertisement
from django.db.models import QuerySet
from django.views import View
from django.views import generic
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


# Create your views here.
class CategoryListView(generic.ListView):
    model = Category

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        super().get(request, *args, **kwargs)

        categories: QuerySet[Category] = self.object_list.order_by("name")

        response: list = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class CategoryDetailView(generic.DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({
            "id": category.id,
            "name": category.name
        }, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
# Create your views here.
class CategoryCreateView(generic.CreateView):
    model = Category
    fields = ["name"]

    def post(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        super().post(request, *args, **kwargs)
        category_data: dict = json.loads(request.body)

        category: Category = Category.objects.create(name=category_data["name"])
        return JsonResponse({
            "id": category.id,
            "name": category.name
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(generic.UpdateView):
    model = Category
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)
        self.object.name = category_data["name"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)

# @method_decorator(csrf_exempt, name='dispatch')
# class AdvertisementListView(generic.ListView):
#     def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
#         super().get(request, *args, **kwargs)
#
#         advertisements: QuerySet[Advertisement] = self.object_list
#         response: list = []
#         for advertisement in advertisements:
#             response.append({
#                 "id": advertisement.id,
#                 "name": advertisement.name,
#                 "author": advertisement.author_id,
#                 "price": advertisement.price,
#                 "description": advertisement.description,
#                 "is_published": advertisement.is_published,
#                 "image": advertisement.image,
#                 "category_id": advertisement.category_id,
#             })
#
#         return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})
#
#
# class AdvertisementDetailView(generic.DetailView):
#     model: Type[Advertisement] = Advertisement
#
#     def get(self, request: HttpRequest, *args: list, **kwargs: dict) -> JsonResponse:
#         advertisement: Advertisement = self.get_object()
#
#         return JsonResponse({
#             "id": advertisement.id,
#             "name": advertisement.name,
#             "author": advertisement.author_id,
#             "price": advertisement.price,
#             "description": advertisement.description,
#             "is_published": advertisement.is_published,
#             "image": advertisement.image,
#             "category_id": advertisement.category_id,
#         }, json_dumps_params={"ensure_ascii": False})
#
#
# #
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class AdvertisementCreateView(generic.CreateView):
#     model = Advertisement
#     fields = ["id", "name""author", "price", "description", "is_published", "image", "category_id"]
#
#     def post(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
#         super().post(request, *args, **kwargs)
#
#         advertisement_data: dict = json.loads(request.body)
#         advertisement: Advertisement = Advertisement.objects.create(**advertisement_data)
#         return JsonResponse({
#             "id": advertisement.id,
#             "name": advertisement.name,
#             "author": advertisement.author_id,
#             "price": advertisement.price,
#             "description": advertisement.description,
#             "is_published": advertisement.is_published,
#             "image": advertisement.image,
#             "category_id": advertisement.category_id,
#         }, json_dumps_params={"ensure_ascii": False})
#