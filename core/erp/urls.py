from django.urls import path

from .views.category.views import CategoryListView

urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='category_list'),
]
