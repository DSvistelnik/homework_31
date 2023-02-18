import json
from typing import Type
from django.core.paginator import Paginator
from ads.models import Category, Advertisement
from django.db.models import QuerySet
from django.views import generic
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from homework_27 import settings


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


# Создаем свои представления Категории
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

# Создаем свои представления Объявлений
class AdvertisementListView(generic.ListView):
    model = Advertisement

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.select_related("author").order_by("-price")
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page", 1)
        page_object = paginator.get_page(page_number)

        advertisements: list = []
        for advertisement in page_object:
            advertisements.append({
                "id": advertisement.id,
                "name": advertisement.name,
                "author_id": advertisement.author_id,
                "author": advertisement.author.first_name,
                "price": advertisement.price,
                "description": advertisement.description,
                "is_published": advertisement.is_published,
                "image": advertisement.image.url if advertisement.image else None,
                "category_id": advertisement.category_id,
            })

        response = {
            "items": advertisements,
            "total": paginator.count,
            "num_pages": paginator.num_pages
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class AdvertisementDetailView(generic.DetailView):
    model: Type[Advertisement] = Advertisement

    def get(self, request: HttpRequest, *args: list, **kwargs: dict) -> JsonResponse:
        advertisement: Advertisement = self.get_object()

        return JsonResponse({
            "id": advertisement.id,
            "name": advertisement.name,
            "author_id": advertisement.author_id,
            "price": advertisement.price,
            "description": advertisement.description,
            "is_published": advertisement.is_published,
            "image": advertisement.image.url if advertisement.image else None,
            "category_id": advertisement.category_id,
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdvertisementCreateView(generic.CreateView):
    model = Advertisement
    fields = ["name", "author", "price", "description", "is_published", "image", "category"]

    def post(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        super().post(request, *args, **kwargs)

        advertisement_data: dict = json.loads(request.body)
        advertisement: Advertisement = Advertisement.objects.create(**advertisement_data)
        return JsonResponse({
            "id": advertisement.id,
            "name": advertisement.name,
            "author_id": advertisement.author_id,
            "price": advertisement.price,
            "description": advertisement.description,
            "is_published": advertisement.is_published,
            "image": advertisement.image.url if advertisement.image else None,
            "category_id": advertisement.category_id,
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdvertisementUpdateView(generic.UpdateView):
    model = Advertisement
    fields = ["name", "author", "price", "description", "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        advertisement_data: dict = json.loads(request.body)
        advertisement = self.get_object()
        advertisement.name = advertisement_data["name"]
        advertisement.author_id = advertisement_data["author_id"]
        advertisement.price = advertisement_data["price"]
        advertisement.description = advertisement_data["description"]
        advertisement.category_id = advertisement_data["category_id"]

        advertisement.save()
        return JsonResponse({
            "id": advertisement.id,
            "name": advertisement.name,
            "author_id": advertisement.author_id,
            "author": advertisement.author.first_name,
            "price": advertisement.price,
            "description": advertisement.description,
            "is_published": advertisement.is_published,
            "image": advertisement.image.url if advertisement.image else None,
            "category_id": advertisement.category_id,
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdvertisementImageUpdateView(generic.UpdateView):
    model = Advertisement
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.first_name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
            "category_id": self.object.category_id,
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdvertisementDeleteView(generic.DeleteView):
    model = Advertisement
    success_url = "/"
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)