from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



# Runners. Must have a number which can be alphanumeric. A sex. An age.
class Runner(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    number = models.CharField(max_length=4, unique=True)                        # e.g. A11, F1, C99, B8
    gender = models.IntegerField(choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    email = models.EmailField(max_length=254, blank=True, default='')
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("number", "last_name")

    def __unicode__(self):
        return self.number

    def __str__(self):
        return f"Number: '{self.number}' - {self.last_name}"

# Team model. Only 6 runners per team.
class Teams(models.Model):
    number = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)], unique=True)
    name = models.CharField(max_length=200)
    club_name = models.CharField(max_length=200)
    runners_A = models.OneToOneField(Runner, on_delete=models.CASCADE, related_name='Runner_A')
    runners_B = models.OneToOneField(Runner, on_delete=models.CASCADE, related_name='Runner_B')
    runners_C = models.OneToOneField(Runner, on_delete=models.CASCADE, related_name='Runner_C')
    runners_D = models.OneToOneField(Runner, on_delete=models.CASCADE, related_name='Runner_D')
    runners_E = models.OneToOneField(Runner, on_delete=models.CASCADE, related_name='Runner_E')
    runners_F = models.OneToOneField(Runner, on_delete=models.CASCADE, related_name='Runner_F')

    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("number", "name")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return f"Number: '{self.number}' - {self.name} {self.club_name}"


class Race(models.Model):
    STARTED = 1
    STOPPED = 0
    STARTED_CHOICES = [(STARTED, 'STARTED'), (STOPPED, 'NOT STARTED')]
    race_started = models.IntegerField(choices=STARTED_CHOICES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)