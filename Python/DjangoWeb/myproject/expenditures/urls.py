from django.urls import path
from .views import *


urlpatterns = [
    path("", all.as_view()),
    path("ravi/", al.as_view()),
]