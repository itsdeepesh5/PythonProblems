
str="172a.17.1.23"
cnt=[]
for i in str.split("."):
  cnt.append(i)
  try:
    if int(i) < 255:
      print("valid")
    else:
      raise ValueError
  except ValueError:
    print("invalid")
    exit
  
