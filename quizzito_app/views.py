from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions
from django.template import loader
from django.urls import reverse
from .forms import Administrators_Login

# Create your views here.
"""
Note Demiz is the same as Emmanuel or Emman or Eddie or Mizbehave, 
or what ever name you know of me, you're kindly asked not to share
this code to ANYONE without the team notice!!!
"""

AdministratorsUsername = "Demiz"
AdministratorsPassword = "1234567"



def score(request):
    global score
    global attempts
    questions = Questions.objects.all().values()
    score = 0 if request.POST else ''
    attempts = 0
    for n, i in enumerate(questions):
        try:
            if request.POST[f'question_{n+1}'] == i['answer']:
                score += 10
        except:
            pass
        try:
            if request.POST[f'question_{n+1}']:
                attempts += 1
        except:
            pass
    print(f'This is attempts: {attempts}')
    return HttpResponseRedirect(reverse('home'))


def homepage(request):
    questions = Questions.objects.all().values()
    content = {
        "questions": enumerate(questions),
        "total": range(len(questions)),
        "score": score,
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(content, request))


def database(request):
    data = Questions.objects.all().values()
    template = loader.get_template('index.html')
    content = {
        "database": data,
        "total": len(data)
    }
    return HttpResponse(template.render(content, request))


def questions_generator(request):
    template = loader.get_template('questions_generator.html')
    content = {}
    return HttpResponse(template.render(content, request))


def qg_algorithm(request):
    Questions.objects.create(
        question=request.POST['question'],
        answer=request.POST['answer'],
        opt1=request.POST['opt1'],
        opt2=request.POST['opt2'],
        opt3=request.POST['opt3'],
        opt4=request.POST['opt4']
    )
    return HttpResponseRedirect(reverse(viewname='database'))


def q_delete(request, q_id):
    question_to_delete = Questions.objects.get(id=q_id)
    question_to_delete.delete()
    return HttpResponseRedirect(reverse('database'))


def update(request, q_id):
    modifier = Questions.objects.get(id=q_id)
    template = loader.get_template('update.html')
    content = {
        "modifier": modifier
    }
    return HttpResponse(template.render(content, request))


def update_algorithm(request, q_id):
    modifier = Questions.objects.get(id=q_id)
    modifier.question = request.POST['question']
    modifier.answer = request.POST['answer']
    modifier.opt1 = request.POST['opt1']
    modifier.opt2 = request.POST['opt2']
    modifier.opt3 = request.POST['opt3']
    modifier.opt4 = request.POST['opt4']
    modifier.save()
    return HttpResponseRedirect(reverse('database'))


def from_database_to_homepage_redirector(request):
    return HttpResponseRedirect(reverse('home'))


def back_to_database(request):
    return HttpResponseRedirect(reverse('database'))



def admin_login_verification(request): 
    template = loader.get_template(template_name='admin_login.html')
    verifier = ""
    if request.POST:
        loginform = Administrators_Login(request.POST or None)
        if loginform.is_valid():
            verifier = 0 if (request.POST['username'] == AdministratorsUsername) & \
                (request.POST['password'] == AdministratorsPassword) else 1
            if not verifier:
                return HttpResponseRedirect(redirect_to=reverse(viewname='database'))
    content = dict(
        form=Administrators_Login(), 
        verifier=verifier,
    )
    return HttpResponse(template.render(content, request))

    