import os
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
      
classes = []
goodf = open("preco1.txt","r")
while True:
  cn = goodf.readline()
  if cn == "":
    break
  pre = goodf.readline()
  co = goodf.readline()
  
  course = Course()
  course.department = cn[0:2]
  course.number = cn[3:]
  classes.append((cn,pre,co))
  course.save()

for (cn,pre,co) in classes:
  print "Parsing reqs for " + cn,
  course = Course.objects.filter(department=cn[0:2], number=cn[3:])[0]
  course.prereqs = parse_reqs(pre[:-1])
  course.coreqs = parse_reqs(co[:-1])
  course.save()
