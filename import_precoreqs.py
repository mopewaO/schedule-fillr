import os
import time
import datetime
import apis
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schedule_fillr.settings")
from www.models import Course, Lecture, Recitation, Clause

def parse_reqs(reqs):
  if reqs == "":
    return None
  
  parens = 0
  fullstring = ""
  tokens = []
  booltype = ""
  for ch in reqs:
    fullstring += ch
    if ch == "(":
      parens += 1
    elif ch == ")":
      parens -= 1
    elif fullstring[-4:] == "and " and parens == 0:
      tokens.append(fullstring[:-5])
      fullstring = ""
      booltype = "and"
    elif fullstring[-3:] == "or " and parens == 0:
      tokens.append(fullstring[:-4])
      fullstring = ""
      booltype = "or"
  if fullstring != "":
    tokens.append(fullstring)
  
  clause = Clause()
  if booltype == "and":
    clause.booland = True
  else:
    clause.booland = False
  clause.save()
  
  for term in tokens:
    if term[0] == "(":
      clause.clauses.add(parse_reqs(term[1:-1]))
    else:
      opts = Course.objects.filter(department=term[0:2], number=term[3:])
      if len(opts) >= 1:
        clause.courses.add(opts[0])
      else:
        ncourse = Course()
        ncourse.department = term[0:2]
        ncourse.number = term[3:]
        ncourse.save()
        clause.courses.add(ncourse)
  clause.save()
  
  return clause

schedule = apis.Scheduling(app_id="574abff5-5e8c-4e9b-9188-b74a8b03fc4c",app_secret_key="RUNXPkingiQ-sGvMkFHwe1We6_8FYhUiIdrCgTC4T2yeSJUUgd-EFEOy")

nsem = ''
today = datetime.date.today()
if today.month in range(1,6):
  nsem = 'F' + str(today.year)[2:]
else:
  nsem = 'S' + str(today.year+1)[2:]
      
classes = []
goodf = open("preco1.txt","r")
while True:
  cn = goodf.readline()
  if cn == "":
    break
  pre = goodf.readline()
  co = goodf.readline()
  
  print "Getting data for " + cn,
  
  course = Course()
  course.department = cn[0:2]
  course.number = cn[3:]
  classes.append((cn,pre,co))
  course.save()
  
  cinfo = schedule.course(nsem, course_number=(cn[0:2]+cn[3:-1]))
  if cinfo != None:
    course.units = int(cinfo["units"])
    course.save()
  
    for linfo in cinfo["lectures"]:
      if linfo["time_start"] != "TBA":
        lecture = Lecture()
        lecture.starttime = linfo["time_start"]
        lecture.endtime = linfo["time_end"]
        lecture.monday = "M" in linfo["days"]
        lecture.tuesday = "T" in linfo["days"]
        lecture.wednesday = "W" in linfo["days"]
        lecture.thursday = "R" in linfo["days"]
        lecture.friday = "F" in linfo["days"]
        lecture.saturday = "S" in linfo["days"]
        lecture.sunday = "U" in linfo["days"]
        lecture.professor = linfo["instructors"]
        lecture.number = linfo["section"][-1:]
        lecture.save()
    
        course.lectures.add(lecture)
        course.save()
    
        if "recitations" in linfo:
          for rinfo in linfo["recitations"]:
            if rinfo["time_start"] != "TBA":
              recitation = Recitation()
              recitation.letter = rinfo["section"]
              recitation.starttime = rinfo["time_start"]
              recitation.endtime = rinfo["time_end"]
              recitation.monday = "M" in rinfo["days"]
              recitation.tuesday = "T" in rinfo["days"]
              recitation.wednesday = "W" in rinfo["days"]
              recitation.thursday = "R" in rinfo["days"]
              recitation.friday = "F" in rinfo["days"]
              recitation.saturday = "S" in rinfo["days"]
              recitation.sunday = "U" in rinfo["days"]
              recitation.save()
      
              lecture.recitations.add(recitation)
              lecture.save()

for (cn,pre,co) in classes:
  print "Parsing reqs for " + cn,
  course = Course.objects.filter(department=cn[0:2], number=cn[3:])[0]
  course.prereqs = parse_reqs(pre[:-1])
  course.coreqs = parse_reqs(co[:-1])
  course.save()
