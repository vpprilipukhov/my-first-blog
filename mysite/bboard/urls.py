from django.urls import path
from .views import index
from .views import by_rubric


urlpatterns = [
    path('', index),
    path('<int:rubric_id>/',by_rubric)
]