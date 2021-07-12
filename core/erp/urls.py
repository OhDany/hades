from django.urls import path

from .views.category.views import CategoryListView, CategoryCreateView, CategoryUpdateView

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/',
         CategoryUpdateView.as_view(), name='category_update'),
]
