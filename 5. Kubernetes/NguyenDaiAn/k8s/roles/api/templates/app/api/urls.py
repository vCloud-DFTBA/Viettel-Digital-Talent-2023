from django.urls import path

from . import views

urlpatterns = [
    path("listusers",views.listUsers,name="list_user"),
    path("getuser/<id>",views.getUser,name="get_user"),
    path("createuser",views.createUser,name="create_user"),
    path("updateuser",views.updateUser,name="update_user"),
    path("deleteuser",views.deleteUser,name="delete_user"),
]
