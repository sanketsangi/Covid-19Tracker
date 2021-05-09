from django.urls import path

from .views import CovidListView

urlpatterns = [
    path('', CovidListView.as_view(), name='index.html'),
]
