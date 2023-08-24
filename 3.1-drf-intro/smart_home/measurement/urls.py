from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateView, MeasurementCreateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
