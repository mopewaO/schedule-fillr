import tempfile
import re

#pass a file, get list of courses w/ lecture/recitation number
def parse_ics_file(f):
	filetxt = f.read()
	courselist = re.split(r"BEGIN:VEVENT", filetxt)
	callist = []
	for course in courselist:
		coursename = re.search(r"SUMMARY:[^:]+:: (\d\d\d\d\d) ([A-Z\d]+)", course)
		if coursename != None:
			callist.append(coursename.group(1) + " " + coursename.group(2))
        return callist
