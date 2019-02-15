import math 
import sys

class Solution:
    # @param A : integer
    # @return a list of integers
    def isPrime(self, n):
      if n ==2:
	return True
	
      if (n%2 ==0) or (n==0):
        return False 
      for i in xrange(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
          return False
      return True 

    def getPrimeList(self,n): 
        lst = [2]
        for i in xrange(3,n):
            if self.isPrime(i):
                lst.append(i)
        return lst
    
    def getprimesum(self, A):
	
      for i in range(2, int(A/2)+1):
        if self.isPrime(i) and self.isPrime(A-i):
          return [i, A-i]
	  
if __name__ == "__main__":
  s = Solution()
  print(s.getprimesum(int(sys.argv[1])))	