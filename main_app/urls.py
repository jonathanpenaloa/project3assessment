from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemList.as_view(), name="item_list"),
    path('item/add/', views.ItemCreate.as_view(), name="item_form"),
    path('item/<int:pk>/delete', views.ItemDelete.as_view(), name="item_delete"),
]