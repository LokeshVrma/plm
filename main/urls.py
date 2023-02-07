from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutUser, name='logout'),

    path('create_item/', views.createItem, name='create_item'),
    path('update_item/<str:pk>', views.updateItem, name='update_item'),
    path('delete_item/<str:pk>', views.deleteItem, name='delete_item'),
    path('item_detail/<str:pk>', views.itemDetail, name="item_detail"),
]