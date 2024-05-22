from django.urls import path
from .views import ObterNumDiv

urlpatterns = [
    path('obter-num-div/', ObterNumDiv.as_view(), name='obter-num-div'),
]
