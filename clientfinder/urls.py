from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name = 'home'),
    path('testView',views.testView, name = 'testview'),
    path('foundView/',views.foundClientsView , name = 'clientel')

]
