from django.db.models.query import QuerySet
from .models import Project, QuestionIterTwo, Questions, Answers, Question, FinalQuestion
from django.forms import ModelForm, fields, TextInput, DateInput, widgets, Textarea, Select, ClearableFileInput, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.contrib.auth.models import User

class CustomMMCF(ModelMultipleChoiceField):
    def label_from_instance(self, user: User):
        return "%s" % user.get_full_name

class CreateProjectForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     """ Grants access to the request object so that only members of the current user
    #     are given as options"""

    #     self.request = kwargs.pop('request')
    #     super(CreateProjectForm, self).__init__(*args, **kwargs)
    #     self.fields['members'].queryset = User.objects.filter(
    #         user=self.request.user.groups.all()[1])

    class Meta:
        model = Project
        members = CustomMMCF(queryset=User.objects.all(), widget=CheckboxSelectMultiple)
        fields = ['title', 'info', 'image' , 'members' , 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "info": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация о проекте'
            }),
            "image": ClearableFileInput(),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата создания'
            })
        }

class CreateQuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['project', 'expert', 'title', 'question1', 'question2', 'question3', 'question4', 'question5']

        widgets = {
            "project": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Проект'
            }),
            "expert": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Автор вопросов'
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "question1": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос 1'
            }),
            "question2": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос 2'
            }),
            "question3": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос 3'
            }),
            "question4": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос 4'
            }),
            "question5": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос 5'
            }),
        }

class CreateAnswersForm(ModelForm):
    class Meta:
        model = Answers
        fields = ['project', 'questions', 'expert', 'comment1', 'comment2', 'comment3',
         'comment4', 'comment5']

        widgets = {
            "project": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Проект'
            }),
            "questions": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Список вопросов'
            }),
            "expert": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Автор вопросов'
            }),
            "comment1": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
            "comment2": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'value': ''
            }),
            "comment3": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'value': ''
            }),
            "comment4": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'value': ''
            }),
            "comment5": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'value': ''
            }),
        }

class CreteQuestionsIterTwo(ModelForm):
    class Meta:
        model = QuestionIterTwo
        questions = ModelMultipleChoiceField(queryset=Question.objects.all(), widget=CheckboxSelectMultiple)
        fields = ['title', 'questions']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
        }

class CreteQuestionsIterThree(ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(CreteQuestionsIterThree, self).__init__(*args, **kwargs)
        self.fields['questions'].queryset = Question.objects.filter(
            iter=2)

    class Meta:
        model = QuestionIterTwo
        questions = ModelMultipleChoiceField(queryset=None, widget=CheckboxSelectMultiple)
        fields = ['title', 'questions']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
        }

class CreteQuestionsIterFour(ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(CreteQuestionsIterFour, self).__init__(*args, **kwargs)
        self.fields['questions'].queryset = Question.objects.filter(
            iter=3)

    class Meta:
        model = QuestionIterTwo
        questions = ModelMultipleChoiceField(queryset=None, widget=CheckboxSelectMultiple)
        fields = ['title', 'questions']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
        }

class CreateFinalQuestion(ModelForm):
    class Meta:
        model = FinalQuestion
        fields = ['project', 'title']

        widgets = {
            "project": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Проект'
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
        }