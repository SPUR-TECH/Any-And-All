from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('review-create/<int:pk>',
         views.ReviewCreateView.as_view(), name='review_create'),
    path('review-update/<int:pk>/<int:id>',
         views.ReviewUpdateView.as_view(), name='review_update'),
    path(
        'review-delete/<int:pk>/<int:id>',
        views.ReviewDeleteView.as_view(), name='review_delete'),
]
