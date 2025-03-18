from django.urls import path
from .views import view_question, start_mock_test, mock_test_result, start_practical_test, practical_test_result

urlpatterns = [

    path('view/',view_question, name="view_question"),
    path("start/", start_mock_test, name="start_mock_test"),
    path("result/<int:test_id>/", mock_test_result, name="mock_test_result"),
    path('pt/start/<int:subject_id>/', start_practical_test, name="practical_test"),
    path('submit/<int:submission_id>/', practical_test_result, name='practical_test_result'),

]








# from django.urls import path
# from .views import start_practical_test, practical_test_result
#
# urlpatterns = [
#     path("practical-test/<int:practical_test_id>/", start_practical_test, name="start_practical_test"),
#     path("practical-test/<int:practical_test_id>/submit/", practical_test_result, name="practical_test_result"),
# ]