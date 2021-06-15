from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('actual', views.actual, name='actual'),
    path('answers', views.lastAnswers, name='answers'),
    path('create_project', views.AddProject.as_view(), name='create_project'),
    path('<int:pk>', views.ProjectDeteilView.as_view(), name='project_detail'),
    path('create_questions', views.createQuestions, name='create_questions'),
    path('create_answers/<int:pk>', views.createAnswers, name='create_answers'),
    path('questions_details/<int:pk>', views.QuestionstDeteilView.as_view(), name='questions_details'),
    path('answers_details/<int:pk>', views.checkAnswers, name='answers_details'),
    path('all_questions', views.allQuestions, name='all_questions'),
    path('questions_iter_two', views.AddQuestionsIterTwo.as_view(), name='questions_iter_two'),
    path('questions_iter_three', views.AddQuestionsIterThree.as_view(), name='questions_iter_three'),
    path('questions_iter_three', views.AddQuestionsIterFour.as_view(), name='questions_iter_three'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('questionnaire_details/<int:pk>', views.QuestionnaireDeteilView.as_view(), name='questionnaire_details'),
    path('final_question', views.createFinalQuestion, name='final_question'),
]