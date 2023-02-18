import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count, Q
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from homework_27 import settings
from users.models import User, Location


# Создание представления Пользователей
class UserListView(generic.ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.annotate(
            total_ads=Count('advertisement', filter=Q(advertisement__is_published=True))).prefetch_related(
            'locations').order_by('username')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page", 1)
        page_object = paginator.get_page(page_number)

        users = []
        for user in page_object:
            users.append({
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "age": user.age,
                "locations": list(map(str, user.locations.all())),
                "total_ads": user.total_ads
            })

        response = {
            "items": users,
            "total": paginator.count,
            "num_pages": paginator.num_pages,
        }

        return JsonResponse(response, safe=False)


class UserDetailView(generic.DetailView):
    model = User

    def get(self, request, *args, **kwargs):

        self.object = self.get_object()

        return JsonResponse({
            "id": self.object.id,
            "username": self.object.username,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "role": self.object.role,
            "age": self.object.age,
            "locations": list(self.object.locations.all().values_list("name", flat=True))
        }, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(generic.CreateView):
    model = User
    fields = ["username", "password", "first_name", "last_name", "role", "age", "locations"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        user = User.objects.create(
            username=user_data["username"],
            password=user_data["password"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role=user_data["role"],
            age=user_data["age"],
        )

        for location in user_data["locations"]:
            location_obj, created = Location.objects.get_or_create(name=location)
            user.locations.add(location_obj)
        user.save()

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "locations": list(user.locations.all().values_list("name", flat=True))
        })


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateViews(generic.UpdateView):
    model = User
    fields = ["username", "password", "first_name", "last_name", "age", "locations"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        user = self.get_object()
        user.username = user_data["username"]
        user.password = user_data["password"]
        user.first_name = user_data["first_name"]
        user.last_name = user_data["last_name"]
        user.age = user_data["age"]

        for location in user_data["locations"]:
            location_obj, created = Location.objects.get_or_create(name=location)
            user.locations.add(location_obj)
        user.save()

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "locations": list(user.locations.all().values_list("name", flat=True))
        })


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(generic.DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"})
