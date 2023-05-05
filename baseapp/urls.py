from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name='home'),
    path('<cat_id>/meals/',views.menumeals, name='menumeals'),
    path('add_cart/<meal_id>/', views.add_cart, name='add_cart'),
    path('cart/', views.cart, name='cart'),
    path('search/', views.search, name='search')
]