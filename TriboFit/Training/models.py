from django.db import models
from User.models import TheUser

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.CharField(max_length=600, blank=False, null=False)
    muscle_group = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField('Training/', blank=False, null=False)
    video = models.FileField('Training/', blank=True)

class ExerciseTraining(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='exercise', on_delete=models.CASCADE)
    series = models.IntegerField(blank=True)
    repetitions = models.IntegerField(blank=True)

class Training(models.Model):
    exercise_training = models.ForeignKey(ExerciseTraining, related_name='exercises', on_delete=models.CASCADE)
    muscle_group = models.CharField(max_length=100, blank=False, null=False)

class TrainingSheet(models.Model):
    user = models.ForeignKey(TheUser, on_delete=models.CASCADE, related_name='TrainingSheet', blank=False, null=False)
    nome = models.CharField(max_length=100, blank=False, null=False)
    training = models.ManyToManyField(Training, related_name='Trainings', blank=False)
    type = models.CharField(max_length=5, choices=(('ABC', 'ABC'), ('ABCD', 'ABCD'), ('ABCDE', 'ABCDE')), blank=False)





