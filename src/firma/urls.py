from django.urls import path
from firma.views import SignView

app_name = 'firmas'

urlpatterns = [
    path('sign/', SignView.as_view()),
]
