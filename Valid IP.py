import re

def checkIP(add):
  m = re.match(r"([0-255].[0-255].[0-255].[0-255])",add )
  if m:
    if add == m.group(0):
      print("Valid IP")
      return True
  print("Not a Valid IP-",add)
  return False


str="0.1.0.0"
print(checkIP(str))
