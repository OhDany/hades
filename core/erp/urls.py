from django.urls import path

from .views.category.views import CategoryListView

app_name = 'erp'

urlpatterns = [
    path('category/list', CategoryListView.as_view(), name='category_list'),
]
