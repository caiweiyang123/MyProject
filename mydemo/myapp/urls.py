# myapp应用的路由文件
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("find/", views.find),
    path("find/<int:sid>", views.find),
    path("find/<int:sid>/<str:name>", views.find,name="find3"),
    re_path(r"^fun/(?P<yy>[0-9]{4})/(?P<mm>[0-9]{1,2})$", views.fun),
    path("update/", views.update),
]
