import math 
import sys

def isPrime(n):
  if (n < 2) or (n==2) :
    return True
  if (n%2 ==0) or (n==0):
    return False 
  for i in range(3, int(math.sqrt(n))+1, 2):
    if n%i == 0:
      return False
  return True 

def getPrimeList(n): 
  lst = [2]
  for i in xrange(3,n):
    if isPrime(i):
       lst.append(i)
  return lst


def getPrimeSum(sum):
  l = getPrimeList(sum)
  for i in l:
    if sum-i in l:
      return (i, sum-i)
	  
if __name__ == "__main__":
  print(getPrimeSum(int(sys.argv[1])))	