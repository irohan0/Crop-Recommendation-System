from django.urls import path
from mlapp import views

urlpatterns = [
    path("",views.pridictor,name='predictor'),
    path("result",views.info,name='result'),
    

]
