from django.db import models
import string

# Create your models here.
class Course(models.Model):
  department = models.IntegerField()
  number = models.IntegerField()
  title = models.CharField(max_length=255)
  units = models.PositiveSmallIntegerField(default=9)
  prereqs = models.OneToOneField('Clause', related_name='prereqs', null=True, blank=True)
  coreqs = models.OneToOneField('Clause', related_name='coreqs', null=True, blank=True)

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
  parent = models.ForeignKey('self', related_name='clauses', null=True, blank=True)
  booland = models.BooleanField()
  
  def __unicode__(self):
    terms = []
    for course in self.courses.all():
      terms.append(str(course.department) + "-" + str(course.number))
    for clause in self.clauses.all():
      terms.append("(" + str(clause) + ")")
    if self.booland:
      return string.join(terms, " and ")
    else:
      return string.join(terms, " or ")
