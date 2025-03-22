from django.shortcuts import render, redirect,  get_object_or_404, HttpResponse
from test_app.models import Subject, Chapter, Question, MockTest, MockTestSubmission, PracticalTest, PracticalTestSubmission
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
    print("sub", submissions)

    total_questions = submissions.count()
    correct_answers = submissions.filter(is_correct=True).count()
    score = (correct_answers / total_questions) * 100 if total_questions else 0
    print("score-mocktest", score)

    return render(request, "mock_test_result.html", {
        "mock_test": mock_test,
        "submissions": submissions,
        "score": score
    })





def subject_list(request):
    subjects = Subject.objects.filter(is_active=True)
    print("all/////////", subjects)
    return render(request, "subject_list.html", {"subjects": subjects})




def select_subject(request, subject_id):
    return redirect("chapter_list", subject_id=subject_id)


def chapter_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    print("sub",subject)
    chapters = Chapter.objects.filter(subject=subject, is_active=True)
    print("////////////////////////////////",chapters)
    return render(request, "chapter_list.html", {"subject": subject, "chapters": chapters})




@login_required(login_url="/auth/login/")
def start_practical_test(request, chapter_id):

    chapter = get_object_or_404(Chapter, id=chapter_id, is_active=True)
    print("chapter",chapter)
    subject = chapter.subject
    student = request.user
    print("student",student)


    practical_test, created = PracticalTest.objects.get_or_create(
        student=student,
        subject=subject,
        organization=subject.organization,
        completed=False
    )

    questions = Question.objects.filter(chapter=chapter).order_by("question_no")

    if request.method == "POST":
        answers = {}
        total_questions = questions.count()
        total_attended = 0
        correct_answers = 0

        for question in questions:
            selected_option = request.POST.get(f"question_{question.id}", "N")
            print("selected", selected_option)
            is_correct = selected_option == question.correct_option

            answers[str(question.id)] = selected_option
            if selected_option != "N":
                total_attended += 1
            if is_correct:
                correct_answers += 1

        score = (correct_answers / total_questions) * 100 if total_questions else 0
        print("score",score)

        PracticalTestSubmission.objects.create(
            practical_test=practical_test,
            student=student,
            subject=subject,
            answers=str(answers),
            score=score,
            unattended=total_questions - total_attended,
            total_attended=total_attended,
            completed=True
        )

        practical_test.completed = True
        practical_test.save()
        print("practicaltest",practical_test)

        messages.success(request, "Practical test submitted successfully.")
        return redirect("practical_test_result", test_id=practical_test.id)

    return render(request, "practical_test.html", {
        "practical_test": practical_test,
        "subject": subject,
        "chapter": chapter,
        "questions": questions,
    })



@login_required
def practical_test_result(request, test_id):

    practical_test = get_object_or_404(PracticalTest, id=test_id, student=request.user)
    submission = PracticalTestSubmission.objects.filter(practical_test=practical_test).first()

    # if not submission:
    #     messages.error(request, "No submission found for this test.")
    #     return redirect("subject_list")

    return render(request, "pratical_test_result.html", {
        "practical_test": practical_test,
        "submission": submission,
    })


def view_test(request):
    return render(request, "test.html")




def add_subject(request):
    if request.method == "POST":
        subject_name = request.POST.get("subject_name")
        organization_id = request.POST.get("organization_id")
        is_active = request.POST.get("is_active") == "on"

        organization = Organization.objects.get(id=organization_id)

        subject = Subject(subject_name=subject_name, organization=organization, is_active=is_active)
        subject.save()
        print("//////////",subject)

        return redirect("subject_list")

    organizations = Organization.objects.all()
    print("organization",organizations)
    return render(request, "add_subject.html", {"organizations": organizations})


def add_chapter(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject_id = request.POST.get("subject_id")
        title = request.POST.get("title")
        is_active = request.POST.get("is_active") == "on"

        subject = Subject.objects.get(id=subject_id)
        print("add_chapter_sub",subject)

        chapter = Chapter(name=name,subject=subject,title=title,is_active=is_active)
        print("////////////////",chapter)
        chapter.save()
        return redirect("view_chp")
    subjects = Subject.objects.all()
    return render(request,"add_chapter.html",{"subject":subjects})


def view_chapter_list(request):
    chapter = Chapter.objects.all()
    return render(request,"view_chapter_list.html",{"chapter":chapter})



def add_question(request):
    if request.method == "POST":

        chapter_id = request.POST.get("chapter_id")
        question_no = request.POST.get("question_no")
        question_text = request.POST.get("question_text")
        option_a = request.POST.get("option_a")
        option_b = request.POST.get("option_b")
        option_c = request.POST.get("option_c")
        option_d = request.POST.get("option_d")
        correct_option = request.POST.get("correct_option")
        year = request.POST.get("year")
        answer = request.POST.get("answer")
        explanation = request.POST.get("explanation")
        verified = request.POST.get("verified") == "on"


        chapter = Chapter.objects.get(id=chapter_id)

        question = Question(
            chapter=chapter,
            question_no=question_no,
            question_text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_option=correct_option,
            year=year,
            answer=answer,
            explanation=explanation,
            verified=verified,


        )
        question.save()
        print("///",question)
        return redirect("view_question")

    chapters = Chapter.objects.all()
    return render(request, "add_question.html", {"chapter":chapters})

