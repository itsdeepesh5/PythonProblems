import re
str=" 2asd sad"
pattern=r"\b[0-9]+"
m=re.match(r'([ ]*)(?P<name>[+-]?[0-9]+)(\D*)', str)
#print("Deepesh", pattern, str)
if m:
    print(m.group('name'))
