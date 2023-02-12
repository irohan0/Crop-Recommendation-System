from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("user",views.user,name="user"),
    path("afilter",views.afilter,name="afilter"),
    path("result",views.result,name="result"),

]
