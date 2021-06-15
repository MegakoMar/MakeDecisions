from typing import final
from django import forms
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from .models import Answers, FinalAnswer, Project, QuestionIterTwo, Questions, Question
from .forms import CreateProjectForm, CreateQuestionsForm, CreateAnswersForm, CreteQuestionsIterTwo, CreateFinalQuestion, CreteQuestionsIterThree, CreteQuestionsIterFour
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from collections import OrderedDict

def projects(request):
    projects = Project.objects.all().order_by('-date')
    finalAnswers = FinalAnswer.objects.all().order_by('-date')
    data = {
        'projects': projects,
        'finalAnswers': finalAnswers
    }
    return render(request, 'projects/projects.html', data)

def actual(request):
    questions = Questions.objects.all().order_by('-date')
    return render(request, 'projects/actual.html', {'questions': questions})

def lastAnswers(request):
    answers = Answers.objects.all().order_by('-date')
    questions = Questions.objects
    data = {
        'answers': answers, 
        'questions': questions
    }
    
    return render(request, 'projects/last_answers.html', data)

class AddProject(CreateView):
    model = Project
    form_class = CreateProjectForm
    template_name = 'projects/create_project.html'
    success_url = reverse_lazy('index')

class ProjectDeteilView(DetailView):
    model = Project
    template_name = 'projects/project_details.html'
    context_object_name = 'project'

def createQuestions(request):
    error = ''
    if request.method == 'POST':
        form = CreateQuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actual')
        else:
            error = 'Данные неверны'

    form = CreateQuestionsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'projects/create_questions.html', data)

class QuestionstDeteilView(DetailView):
    model = Questions
    template_name = 'projects/questions_details.html'
    context_object_name = 'questions'

def createAnswers(request, pk):
    questionIterTwo = QuestionIterTwo.objects.get(id=pk)
    questions = questionIterTwo.questions.all
    error = ''
    if request.method == 'POST':
        form = CreateAnswersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('answers')
        else:
            error = 'Данные неверны'

    form = CreateAnswersForm()
    data = {
        'form': form,
        'error': error,
        'id': pk,
        'questions': questions
    }
    return render(request, 'projects/create_answers.html', data)

class AnswerstDeteilView(DetailView):
    model = Answers
    template_name = 'projects/answers_details.html'
    context_object_name = 'answers'

def checkAnswers(request, pk):
    questionIterTwo = QuestionIterTwo.objects.get(id=1)
    questions = questionIterTwo.questions.all
    answer = Answers.objects.get(id=pk)

    data = {
        'questions': questions,
        'answer': answer,
    }
    return render(request, 'projects/answers_details.html', data)

def allQuestions(request):
    questions = Questions.objects.all()
    question = Question.objects.all()
    iter = len(Questions.objects.all()) / 5
    for item in questions:
        question1 = Question(title=item.question1, project=item.project, iter = iter)
        if not question.filter(title=question1.title).exists():
            question1.save()

        question2 = Question(title=item.question2, project=item.project, iter = iter)
        if not question.filter(title=question2.title).exists():
            question2.save()
    
        question3 = Question(title=item.question3, project=item.project, iter = iter)
        if not question.filter(title=question3.title).exists():
            question3.save()
            
        question4 = Question(title=item.question4, project=item.project, iter = iter)
        if not question.filter(title=question4.title).exists():
            question4.save()
            
        question5 = Question(title=item.question5, project=item.project, iter = iter)
        if not question.filter(title=question5.title).exists():
            question5.save()
    
    if request.method == 'POST':
        projectTitle = request.POST['project']
        iter = request.POST['iter']
        if projectTitle and iter:
            project = Project.objects.get(title=projectTitle)
            question = question.filter(project=project, iter = iter)
        elif projectTitle:
            project = Project.objects.get(title=projectTitle)
            question = question.filter(project=project)
        elif iter:
            question = question.filter(iter = iter)

    data = {
        'questions': question,
        'projects': Project.objects.all(),
        'iter': int(iter)
    }
    return render(request, 'projects/all_questions.html', data)

class AddQuestionsIterTwo(CreateView):
    model = QuestionIterTwo
    form_class = CreteQuestionsIterTwo
    template_name = 'projects/questions_iter_two.html'
    success_url = reverse_lazy('questionnaire')

class AddQuestionsIterThree(CreateView):
    model = QuestionIterTwo
    form_class = CreteQuestionsIterThree
    template_name = 'projects/questions_iter_two.html'
    success_url = reverse_lazy('questionnaire')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(AddQuestionsIterThree, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class AddQuestionsIterFour(CreateView):
    model = QuestionIterTwo
    form_class = CreteQuestionsIterFour
    template_name = 'projects/questions_iter_two.html'
    success_url = reverse_lazy('questionnaire')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(AddQuestionsIterFour, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

def questionnaire(request):
    questionIterTwo = QuestionIterTwo.objects.all().order_by('-date')
    questionsAll = Question.objects.all()
    
    questions = Question.objects.filter(iter=2)
    data = {
        'questions': questions,
        'questionIterTwo': questionIterTwo
    }
    return render(request, 'projects/questionnaire.html', data)

class QuestionnaireDeteilView(DetailView):
    model = QuestionIterTwo
    template_name = 'projects/questionnaire_details.html'
    context_object_name = 'questionIterTwo'

def createFinalQuestion(request):
    error = ''
    if request.method == 'POST':
        form = CreateFinalQuestion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questionnaire')
        else:
            error = 'Данные неверны'

    form = CreateFinalQuestion()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'projects/final_question.html', data)
