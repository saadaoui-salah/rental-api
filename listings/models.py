from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser
User = get_user_model()


class Property(models.Model):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    RENT = "RENT"

    status_choices = [
        (PENDING, "Pending"),
        (ACTIVE, "Active"),
        (RENT, "Rent"),
        ]

    user = models.ForeignKey(User,limit_choices_to={'user_type':CustomUser.SELLER}, on_delete=models.CASCADE)
    price = models.FloatField(max_length=100)
    status = models.CharField(max_length=100, choices=status_choices)
    address = models.CharField(max_length=200)
    unit_number = models.CharField(max_length=200)
    video = models.FileField(upload_to="properties/videos", null=True, blank=True)
    
class Image(models.Model):
    property_name = models.ForeignKey(Property, on_delete=models.CASCADE)
    iamge = models.ImageField(upload_to="properties/iamges")

class DetailsSection(models.Model):
    property_name = models.ForeignKey(Property, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class StepSection(models.Model):
    details_section = models.ForeignKey(DetailsSection, on_delete=models.CASCADE)

class Question(models.Model):
    TEXT = "TEXT"
    NUMBER = "NUMBER"
    MULTIPLE_CHOICES = "MULTIPLE_CHOICES"
    SINGLE_CHOICE = "SINGLE_CHOICE"

    field_choices = [
        (TEXT, "TEXT"),
        (NUMBER, "NUMBER"),
        (MULTIPLE_CHOICES, "MULTIPLE_CHOICES"),
        (SINGLE_CHOICE, "SINGLE_CHOICE"),
    ]


    details_section = models.ForeignKey(StepSection, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    question = models.CharField(max_length=300)
    question = models.CharField(max_length=100, choices=field_choices)


class Answer(models.Model):
    qustion = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class QuestionChoice(models.Model):
    qustion = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices = models.CharField(max_length=200)
    multiple = models.BooleanField(default=False)

class AnswerChoice(models.Model):
    qustion = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    