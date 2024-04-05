from django.urls import path
from . import views

urlpatterns = [
    path("", views.view1),
    # path("transactions", views.transactions),
    path("transactions", views.transactions)
]