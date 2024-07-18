from django.urls import path
from app import views

urlpatterns = [
    path("", views.userList, name="users"),
    path("detail/<str:pk>", views.userDetail, name="detail"),
    path("create", views.userCreate, name="create"),
    path("update/<str:pk>", views.userUpdate, name="update"),
    path("delete/<str:pk>", views.userDelete, name="delete")

]