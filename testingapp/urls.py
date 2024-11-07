from rest_framework.urls import path
from . import views

urlpatterns = [
    path('logintest/',views.login),
    path('signuptest/',views.signup),
    path('getalltest/',views.getall),
    path('getbyid/<int:id>',views.getbyid),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]
