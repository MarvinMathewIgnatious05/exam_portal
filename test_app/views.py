from django.shortcuts import render, redirect,  get_object_or_404, HttpResponse
from test_app.models import Subject, Question, MockTest, MockTestSubmission, PracticalTest, PracticalTestSubmission
from django.contrib.auth.decorators import login_required
from .forms import MockTestSubmissionForm
from django.utils.timezone import now
from datetime import timedelta
from student.models import Organization
from django.contrib import messages





def view_question(request):
   qn = Question.objects.all().values()
   # print("qqqqqqqqqqqqqq",qn)
   return render(request,"view_question.html",{"qn":qn})




@login_required(login_url="/auth/login/")
def start_mock_test(request):
    if request.user.is_anonymous:
        messages.error(request, "You must be logged in to start the test.")
        return redirect("authentication:user_login")

    student = request.user
    print("////////////",student)

    mock_test, created = MockTest.objects.get_or_create(student=student, completed=False)
    questions = Question.objects.all().order_by("question_no")
    print('///////////',questions)

    if request.method == "POST":
        for question in questions:
            selected_option = request.POST.get(f"question_{question.id}")
            print("///////////////",selected_option)
            is_correct = selected_option == question.correct_option if selected_option else False


            MockTestSubmission.objects.create(
                mock_test=mock_test,
                student=student,
                question=question,
                selected_option=selected_option if selected_option else "N",
                is_correct=is_correct,

            )

        mock_test.completed = True
        mock_test.save()
        print("/////////",mock_test)
        return redirect("mock_test_result", test_id=mock_test.id)

    return render(request, "mock_test.html", {"questions": questions})





@login_required
def mock_test_result(request, test_id):

    mock_test = get_object_or_404(MockTest, id=test_id, student=request.user)
    print("mock_test",mock_test)
    submissions = MockTestSubmission.objects.filter(mock_test=mock_test)
    print("sub",submissions)

    total_questions = submissions.count()
    correct_answers = submissions.filter(is_correct=True).count()
    score = (correct_answers / total_questions) * 100 if total_questions else 0

    return render(request, "mock_test_result.html", {
        "mock_test": mock_test,
        "submissions": submissions,
        "score": score
    })







@login_required(login_url="/auth/login/")
def start_practical_test(request, subject_id):


    student = request.user
    practical_test, created = PracticalTest.objects.get_or_create(
        student=student,
        subject_id=subject_id,
        completed=False
    )

    questions = Question.objects.filter(chapter__subject_id=subject_id).order_by("question_no")

    if request.method == "POST":
        total_attended = 0
        correct_answers = 0
        submitted_answers = {}

        for question in questions:
            selected_option = request.POST.get(f"question_{question.id}")
            print("selected",selected_option)
            is_correct = selected_option == question.correct_option if selected_option else False

            if selected_option:
                total_attended += 1
                print("total/////////////////////",total_attended)
                submitted_answers[question.id] = selected_option
                if is_correct:
                    correct_answers += 1

        score = (correct_answers / questions.count()) * 100 if questions.exists() else 0
        print("//////////////////////",score)

        submission = PracticalTestSubmission.objects.create(
            practical_test=practical_test,
            student=student,
            subject=practical_test.subject,
            answers=str(submitted_answers),
            total_attended=total_attended,
            unattended=questions.count() - total_attended,
            score=score,
            test_average_time=timedelta(seconds=120),
            completed=True,
            submitted_at=now(),
        )

        practical_test.completed = True
        practical_test.save()
        print("pppppppppppppppppppp",practical_test)

        return redirect("practical_test_result", submission_id=submission.id)

    return render(request, "practical_test.html", {
        "practical_test": practical_test,
        "questions": questions,
    })





@login_required
def practical_test_result(request, submission_id):

    submission = get_object_or_404(PracticalTestSubmission, id=submission_id, student=request.user)
    # print("ssssssssssssssss",submission)

    return render(request, "pratical_test_result.html", {
        "submission": submission,
    })