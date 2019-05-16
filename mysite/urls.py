from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path("<int:id>", views.index, name="index"),       # "<int:id>" означает что в адресной строке необходимо ввести еще
     #                                                    # целочисленное значение которое в последствии будет иметь имя
     #                                                    # атрибута "id"
     # path("<str:name>", views.by_name, name="by_name"), # <str:name> аналогично с первым примером, но в адресной
     # path("<int:id>", views.base, name="base"),  # строке нужно ввести строку
     # path("create/", views.create, name="create"),

    ]