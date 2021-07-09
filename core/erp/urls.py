from django.urls import path

from .views.category.views import category_list

urlpatterns = [
    path('category/list', category_list, name='category_list'),
]
