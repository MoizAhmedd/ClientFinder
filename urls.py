from django.urls import path
from . import views

urlpatterns = [
    path('testView',views.testView, name = 'testview'),
    path('foundView/<str:wanted_location>/<str:keywords>/<str:max_radius>',views.foundClientsView , name = 'clientel')

]
