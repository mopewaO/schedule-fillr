import urllib2
import string
import re
import itertools

urlstart = "http://coursecatalog.web.cmu.edu"
urls = ["/servicesandoptions/intercollegeprograms/bxaintercollege/courses/",
        "/servicesandoptions/intercollegeprograms/courses/",
        "/servicesandoptions/departmentofathleticsandphysicaleducation/courses/",
        "/servicesandoptions/rotc/courses/",
        "/carnegieinstituteoftechnology/departmentofbiomedicalengineering/courses/",
        "/carnegieinstituteoftechnology/departmentofchemicalengineering/courses/",
        "/carnegieinstituteoftechnology/departmentofcivilandenvironmentalengineering/courses/",
        "/carnegieinstituteoftechnology/departmentofelectricalandcomputerengineering/courses/",
        "/carnegieinstituteoftechnology/departmentofengineeringandpublicpolicy/courses/",
        "/carnegieinstituteoftechnology/materialsscienceandengineering/courses/",
        "/carnegieinstituteoftechnology/departmentofmechanicalengineering/courses/",
        "/collegeoffinearts/courses/",
        "/collegeoffinearts/schoolofarchitecture/courses/",
        "/collegeoffinearts/schoolofart/courses/",
        "/collegeoffinearts/schoolofdesign/courses/",
        "/collegeoffinearts/schoolofdrama/courses/",
        "/collegeoffinearts/schoolofmusic/courses/",
        "/melloncollegeofscience/departmentofbiologicalsciences/courses/",
        "/melloncollegeofscience/departmentofchemistry/courses/",
        "/melloncollegeofscience/departmentofmathematicalsciences/courses/",
        "/melloncollegeofscience/departmentofphysics/courses/",
        "/melloncollegeofscience/courses/",
        "/dietrichcollegeofhumanitiesandsocialsciences/departmentofenglish/courses/",
        "/dietrichcollegeofhumanitiesandsocialsciences/departmentofhistory/courses/",
        "/dietrichcollegeofhumanitiesandsocialsciences/departmentofmodernlanguages/courses/",
        "/dietrichcollegeofhumanitiesandsocialsciences/departmentofphilosophy/courses/",
        "/dietrichcollegeofhumanitiesandsocialsciences/departmentofpsychology/courses/",
        "/dietrichcollegeofhumanitiesandsocialsciences/departmentofsocialanddecisionsciences/courses/",
        "/dietrichcollegeofhumanitiesandsocialsciences/departmentofstatistics/courses/",
        "/dietrichcollegeofhumanitiesandsocialsciences/courses/",
        "/dietrichcollegeofhumanitiesandsocialsciences/informationsystems/courses/",
        "/dietrichcollegeofhumanitiesandsocialsciences/undergraduateeconomicsprogram/courses/",
        "/schoolofcomputerscience/courses/",
        "/tepper/undergraduatebusinessadministrationprogram/courses/",
        "/tepper/undergraduateeconomicsprogram/courses/"]

precolist = []

for url in urls:
    urlhtml = urllib2.urlopen(urlstart+url).read()
    startidx = string.find(urlhtml, "<a name=\"courseinventory\">")
    endidx = string.find(urlhtml, "endbody")
    coursehtml = urlhtml[startidx:endidx]
    courselist = re.split(r"<dl class=\"courseblock\">", coursehtml)
    for course in courselist:
        coursename = re.search(r"<dt class=\"keepwithnext\">(\d\d-\d\d\d)", course)
        prereqs = re.search(r"Prerequisites?: ([^<]+)<br />", course)
        while prereqs != None and re.search(r"(\d\d-\d\d\d)", prereqs.group(1)) == None:
            prereqs = re.search(r"Prerequisites?: ([^<]+)<br />", prereqs.string[prereqs.lastindex:])
        coreqs = re.search(r"Corequisites?: ([^<]+)<br />", course)
        while coreqs != None and re.search(r"\d\d-\d\d\d", coreqs.group(1)) == None:
            coreqs = re.search(r"Corequisites?: ([^<]+)<br />", coreqs.string[coreqs.lastindex:])
        if prereqs == None:
            pre = ""
        else:
            pre = prereqs.group(1)
        if coreqs == None:
            co = ""
        else:
            co = coreqs.group(1)
        if coursename != None:
            precolist.append((coursename.group(1), pre, co))


for p in precolist:
    print(p)
