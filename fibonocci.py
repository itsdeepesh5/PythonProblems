import time
cache={}
def fib(n):

    if n in cache:
        return cache[n]

    print('Processing',n)
    if n==0:
        value= 0
    elif n == 1:
        value = 1
    elif n==2:
        value=1
    elif n >=2:
        value=fib(n-1) + fib(n-2)
    cache[n]= value
    return value

t0=time.time()
for i in range(0,10):
    print(fib(i))
t1=time.time()
print("Time taken", t1-t0)
