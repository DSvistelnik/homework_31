from users import views
from django.urls import path

urlpatterns = [
    path('', views.UserListView.as_view(), name="user_list"),
    path('<int:pk>/', views.UserDetailView.as_view(), name="user_detail"),
    path('create/', views.UserCreateView.as_view(), name="user_create"),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name="user_delete"),
    path('<int:pk>/update/', views.UserUpdateViews.as_view(), name="user_update"),
]
