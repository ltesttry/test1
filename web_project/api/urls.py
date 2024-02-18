from django.urls import path
from .views import ItemList, ItemDetail, LocationList, LocationDetail


urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemList.as_view()),
    path('location/', ItemList.as_view()),
    path('location/<int:pk>/', ItemList.as_view()),
]
