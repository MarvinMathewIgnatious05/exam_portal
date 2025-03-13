from django.shortcuts import render, redirect,  get_object_or_404
from .models import MockTest, MockTestSubmission, Question
from .forms import MockTestSubmissionForm
from django.utils.timezone import now
from datetime import timedelta
from student.models import Organization
from django.contrib import messages





def view_question(request):
   qn = Question.objects.all().values()
   # print("qqqqqqqqqqqqqq",qn)
   return render(request,"view_question.html",{"qn":qn})





def start_mock_test(request):

    student = request.user
    mock_test, created = MockTest.objects.get_or_create(student=student, completed=False)
    questions = Question.objects.all().order_by("question_no")

    if request.method == "POST":
        for question in questions:
            selected_option = request.POST.get(f"question_{question.id}")
            is_correct = selected_option == question.correct_option if selected_option else False


            MockTestSubmission.objects.create(
                mock_test=mock_test,
                student=student,
                question=question,
                selected_option=selected_option if selected_option else "N",
                is_correct=is_correct
            )

        mock_test.completed = True
        mock_test.save()
        return redirect("mock_test_result", test_id=mock_test.id)

    return render(request, "mock_test.html", {"questions": questions})













def mock_test_result(request, test_id):

    mock_test = get_object_or_404(MockTest, id=test_id, student=request.user)
    submissions = MockTestSubmission.objects.filter(mock_test=mock_test)

    total_questions = submissions.count()
    correct_answers = submissions.filter(is_correct=True).count()
    score = (correct_answers / total_questions) * 100 if total_questions else 0

    return render(request, "mock_test_result.html", {
        "mock_test": mock_test,
        "submissions": submissions,
        "score": score
    })
