from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.pivot_data, name='pivot_data'),
    path('products/', views.products, name='products'),
    path('accounts/', views.accounts, name='accounts'),
    path('add-product/', views.add_product, name='add-product'),
    path('edit-product/', views.edit_product, name='edit-product')
]