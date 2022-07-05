from django.db import models


# Create your models here.
class Test(models.Model):
    name_test = models.CharField(max_length=100, verbose_name="Name")
    description_test = models.CharField(max_length=255, verbose_name="Description")
    date_test = models.DateTimeField(verbose_name='Date')


class Questions(models.Model):
    question_text = models.CharField(max_length=100)
    photo = models.FileField(upload_to='static/questions')
    test_num = models.ForeignKey(Test, on_delete=models.CASCADE, default='')


class Answer(models.Model):
    answer_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0,blank=True)
    question_num = models.ForeignKey(Questions, on_delete=models.CASCADE, default='')
