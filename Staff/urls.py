from django.urls import path
from Staff.views import inicio, index


urlpatterns = [
    path('', inicio),
    path('index/', index)
]
