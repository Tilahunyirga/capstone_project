from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView , UserDetailView, UserListCreateView

urlpatterns = [
    path('/list/', ProductListView.as_view(), name='product-list'),
    path('/search/', ProductListView.as_view(), name='product-search'),
    path('/create/', ProductCreateView.as_view(), name='product-create'),
    path('/detail/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('/update/<int:id>/', ProductUpdateView.as_view(), name='product-update'),
    path('/delete/<int:id>/', ProductDeleteView.as_view(), name='product-delete'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),  # List and create users
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Retrieve, update, delete users
]
