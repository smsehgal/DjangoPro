import re
match = re.compile(r'^(?=.{4,}$)(?:[a-zA-Z\d]+(?:(?:\||_)[a-zA-Z\d])*)+$')
s = "Ankit9Mittal"
mo = match.search(s)
print(mo.group())