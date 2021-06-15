from django.db import models
from django.db.models.fields.files import ImageField
from django.utils import timezone
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField('Название', max_length=250)
    info = models.TextField('Информация')
    image = models.ImageField(null=True, blank=True)
    members = models.ManyToManyField(User)
    date = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
class Questions(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField('Дата создания', default=timezone.now)
    expert = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField('Название', max_length=250, blank=True)
    question1 = models.TextField('Вопрос 1')
    question2 = models.TextField('Вопрос 2', null=True, blank=True)
    question3 = models.TextField('Вопрос 3', null=True, blank=True)
    question4 = models.TextField('Вопрос 4', null=True, blank=True)
    question5 = models.TextField('Вопрос 5', null=True, blank=True)

    class Meta:
        verbose_name = 'Список вопросов'
        verbose_name_plural = 'Списки вопросов'

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField('Вопрос', max_length=250)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    iter = models.IntegerField('Номер итерации', null=True, default=1)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title

class QuestionIterTwo(models.Model):
    title = models.CharField('Название опроса', max_length=250, blank=True)
    questions = models.ManyToManyField(Question)
    date = models.DateTimeField('Дата создания', default=timezone.now)

    class Meta:
        verbose_name = 'Вопрос итерации 2'
        verbose_name_plural = 'Вопросы итерации 2'

    def __str__(self):
        return self.title

class Answers(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField('Дата создания', default=timezone.now)
    questions = models.ForeignKey(QuestionIterTwo, on_delete=models.CASCADE, null=True)
    expert = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment1 = models.TextField('Комментарий к вопросу 1', null=True, blank=True)
    comment2 = models.TextField('Комментарий к вопросу 2', null=True, blank=True)
    comment3 = models.TextField('Комментарий к вопросу 3', null=True, blank=True)
    comment4 = models.TextField('Комментарий к вопросу 4', null=True, blank=True)
    comment5 = models.TextField('Комментарий к вопросу 5', null=True, blank=True)

    class Meta:
        verbose_name = 'Список ответов'
        verbose_name_plural = 'Списки ответов'
    
class FinalQuestion(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    title = models.CharField('Название опроса', max_length=250, blank=True)
    date = models.DateTimeField('Дата создания', default=timezone.now)

    class Meta:
        verbose_name = 'Итоговый вопрос'
        verbose_name_plural = 'Итоговые вопросы'

    def __str__(self):
        return self.title


class FinalAnswer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(FinalQuestion, on_delete=models.CASCADE, null=True)
    expert = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField('Дата создания', default=timezone.now)
    comment = models.TextField('Комментарий к вопросу 1', null=True, blank=True)

    class Meta:
        verbose_name = 'Итоговый ответ'
        verbose_name_plural = 'Итоговые ответы'
