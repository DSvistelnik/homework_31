import json

from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Advertisement
from django.db.models import QuerySet
from django.views import generic
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from ads.serializers import AdSerializer


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


class AdViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer

    def list(self, request, *args, **kwargs):
        categories = request.GET.getlist("cat")
        if categories:
            self.queryset = self.queryset.filter(category__in=categories)

        text = request.GET.get("text")
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get("location")
        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)

        price_from = request.GET.get("price_from")
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        price_to = request.GET.get("price_to")
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)
