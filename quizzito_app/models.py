from django.db import models as m

# Create your models here.
class Questions(m.Model):
    question = m.CharField(max_length=255)
    answer = m.CharField(max_length=255)
    opt1 = m.CharField(max_length=255)
    opt2 = m.CharField(max_length=255)
    opt3 = m.CharField(max_length=255)
    opt4 = m.CharField(max_length=255)
    