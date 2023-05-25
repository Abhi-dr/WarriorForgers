from django.shortcuts import render, redirect
from .models import Registration_Quiz, OLQ_Quiz
from accounts.models import Student, Mentor
from django.shortcuts import get_object_or_404

# ====================================== OLQ TEST START ======================================

def olq_test(request):
    
    user = request.user

    student = get_object_or_404(Student, user_ptr=user)
    
    parameters = {
        'student': student
    }
    
    return render(request, 'preparations/olq_test.html', parameters)


def olq_instructions(request):
    user = request.user

    student = get_object_or_404(Student, user_ptr=user)
    
    parameters = {
        'student': student
    }
    return render(request, 'preparations/instructions.html', parameters)


def olq_quiz(request):
    
    user = request.user

    student = get_object_or_404(Student, user_ptr=user)
    
    if 'user_answers' not in request.session:
        request.session['user_answers'] = {}
        request.session['question_index'] = 0
        questions = OLQ_Quiz.objects.order_by(
            '?')[:10]  # Randomly select 10 questions
        request.session['questions'] = [question.id for question in questions]

    question_index = request.session['question_index']
    questions = OLQ_Quiz.objects.filter(
        id__in=request.session['questions'])
    total_questions = len(request.session['questions'])

    if question_index >= total_questions:
        return redirect('olq_result')

    question = questions[question_index]
    context = {'question': question, 'question_index': question_index +
               1, 'total_questions': total_questions, 'student': student}
    return render(request, 'preparations/quiz.html', context)


def olq_next_question(request):
    if request.method == 'POST':
        question_index = request.session['question_index']
        questions = OLQ_Quiz.objects.filter(
            id__in=request.session['questions'])
        total_questions = len(request.session['questions'])

        if question_index < total_questions:
            request.session['question_index'] += 1

        question_id = str(questions[question_index].id)
        user_answer = request.POST.get(question_id)
        request.session['user_answers'][question_id] = user_answer

        if question_index >= total_questions - 1:
            return redirect('olq_result')

    return redirect('olq_quiz')


def olq_result(request):
    
    user = request.user

    student = get_object_or_404(Student, user_ptr=user)
    
    questions = OLQ_Quiz.objects.filter(
        id__in=request.session['questions'])
    user_answers = request.session.get('user_answers', {})

    correct_answers = []
    incorrect_answers = []
    total_questions = len(request.session['questions'])

    # Check user's answers against correct answers
    for question in questions:
        answer = user_answers.get(str(question.id))
        if answer == question.answer:
            correct_answers.append(question)
        else:
            incorrect_answers.append((question, question.answer, answer))

    success_percentage = int(
        (len(correct_answers) / total_questions) * 100 if total_questions > 0 else 0)

    user = request.user

    student = get_object_or_404(Student, user_ptr=user)

    if success_percentage >= 75:
        student.is_registered = True
        context = {
            'correct_answers': correct_answers,
            'incorrect_answers': incorrect_answers,
            'total_questions': total_questions,
            'success_percentage': success_percentage,
            'student': student
            }

    else:
        mentors = Mentor.objects.filter(
            experties_field_of_interest=student.field_of_interest)
        context = {
            'correct_answers': correct_answers,
            'incorrect_answers': incorrect_answers,
            'total_questions': total_questions,
            'success_percentage': success_percentage,
            'mentors': mentors,
            'student': student
        }

    return render(request, 'preparations/result.html', context)


def olq_reset_quiz(request):
    request.session.pop('user_answers', None)
    request.session.pop('question_index', None)
    request.session.pop('questions', None)
    return redirect('olq_instructions')

# ====================================== OLQ TEST END ======================================

