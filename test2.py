import re

def checkIP(add):
  #matchObj=re.match(r"([0-255]\.[0-255]\.[0-255]\.[0-255])",add)
  add="240.172.1.1"
  m = re.match(r"([0-255].[0-255].[0-255].[0-255])",add )
  #matchObj=re.match(r"([\w+] [\w+])",add)
  if m:
    if add == m.group(0):
      print("Valid IP")
      return True
    print("Not a Valid IP",m.group(0))
  return False

str="Deepesh Rana, abc"
#str="172.17.1.23"
print(checkIP(str))
