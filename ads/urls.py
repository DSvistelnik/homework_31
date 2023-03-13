from rest_framework import routers

from ads import views
from django.urls import path
from django.conf.urls.static import static

from ads.views import AdViewSet, CategoryViewSet
from homework_27 import settings

ad_router = routers.SimpleRouter()
ad_router.register("ad", AdViewSet)

cat_router = routers.SimpleRouter()
cat_router.register("cat", CategoryViewSet)


urlpatterns = [
    path("selection/", views.SelectionListView.as_view(), name="selection_list_view"),
    path("selection/<int:pk>/", views.SelectionDetailView.as_view(), name="selection_detail_view"),
    path("selection/<int:pk>/update/", views.SelectionUpdateView.as_view(), name="selection_update_view"),
    path("selection/<int:pk>/delete/", views.SelectionDeleteView.as_view(), name="selection_delete_view"),
    path("selection/create/", views.SelectionCreateView.as_view(), name="selection_create_view"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += ad_router.urls
urlpatterns += cat_router.urls
