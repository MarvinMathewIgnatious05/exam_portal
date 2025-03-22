from django.urls import path
from .views import (view_question, start_mock_test, mock_test_result, start_practical_test, practical_test_result,
                    subject_list, select_subject, chapter_list, view_test, add_subject, add_chapter, view_chapter_list,
                    add_question)

urlpatterns = [

    path('view/qn/',view_question, name="view_question"),
    path("start/", start_mock_test, name="start_mock_test"),
    path("result/<int:test_id>/", mock_test_result, name="mock_test_result"),
    path('pt/start/<int:chapter_id>/', start_practical_test, name="practical_test"),
    path('submit/<int:test_id>/', practical_test_result, name='practical_test_result'),
    path("subjects/", subject_list, name="subject_list"),
    path("subjects/<int:subject_id>/", select_subject, name="select_subject"),
    path("subjects/<int:subject_id>/chapters/", chapter_list, name="chapter_list"),
    path("view_test/",view_test, name="test"),
    path("add/sub/", add_subject, name="add_sub"),
    path("add/chp/", add_chapter, name="add_chp"),
    path("view/chp/", view_chapter_list, name="view_chp"),
    path("add/qn/", add_question, name="add_qn"),

]






