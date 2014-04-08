from django.db import models

# Create your models here.
class Course(models.Model):
  department = models.IntegerField()
  number = models.IntegerField()
  title = models.CharField(max_length=255)
  units = models.PositiveSmallIntegerField(default=9)
  prereqs = models.OneToOneField('Clause', related_name='prereqs')
  coreqs = models.OneToOneField('Clause', related_name='coreqs')

class Lecture(models.Model):
  number = models.PositiveSmallIntegerField(default=1)
  starttime = models.TimeField('lecture start time')
  endtime = models.TimeField('lecture end time')
  monday = models.BooleanField()
  tuesday = models.BooleanField()
  wednesday = models.BooleanField()
  thursday = models.BooleanField()
  friday = models.BooleanField()
  saturday = models.BooleanField()
  sunday = models.BooleanField()
  professor = models.CharField(max_length=255)
  location = models.CharField(max_length=255)

class Recitation(models.Model):
  letter = models.CharField(max_length=1)
  starttime = models.TimeField('lecture start time')
  endtime = models.TimeField('lecture end time')
  monday = models.BooleanField()
  tuesday = models.BooleanField()
  wednesday = models.BooleanField()
  thursday = models.BooleanField()
  friday = models.BooleanField()
  saturday = models.BooleanField()
  sunday = models.BooleanField()
  lectures = models.ManyToManyField(Lecture)

class Clause(models.Model):
  courses = models.ManyToManyField(Course)
  parent = models.ForeignKey('self', related_name='clauses')
  booland = models.BooleanField()
