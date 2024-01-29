from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipePostList.as_view(), name='home'),
    path("register/",views.RegisterUserView,name="register")
]