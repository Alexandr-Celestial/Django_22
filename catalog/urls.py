from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductContactsView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryProductsListView

app_name=CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ProductContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_confirm_delete/<int:pk>', ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('product_list_category/<int:pk>', CategoryProductsListView.as_view(), name='product_list_category'),
]