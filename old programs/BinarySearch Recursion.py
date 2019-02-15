
def BinarySearch(a, target):
  start=0
  end = len(a) -1
  return interimSearch(a, target)
   
def interimSearch(a, target):
  if(len(a) ==0):
    return False
  
  start=0
  end = len(a) -1
  while (start < end):
    middle = (start+end)//2

    if (a[middle] == target):
      return True

    if (target < a[middle]) :
      end = middle 
    else:
      start = middle 
  return False  

def main():
  target= raw_input()
  a = [i for i in range(1,100) if i%2 ==0]
  print('Searching -->', target)
  print(' In list-' ,a)
  print('Results', BinarySearch(a, int(target)))

if __name__ == '__main__':
  main()