from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("delete_user/<id>",views.deleteUser,name="delete_user"),
    path("update_user/<id>",views.updateUser,name="update_user"),
]
