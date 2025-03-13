from django.urls import path
from .views import view_question, start_mock_test, mock_test_result

urlpatterns = [

    path('view/',view_question, name="view_question"),
    path("start/", start_mock_test, name="start_mock_test"),
    path("result/<int:test_id>/", mock_test_result, name="mock_test_result"),


]


