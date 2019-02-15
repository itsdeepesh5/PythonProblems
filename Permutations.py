n=[1,2,3]
output= {(1,2,3), (2,1,3), (1,3,2),(3,1,2), (2,3,1), (3,2,1)}
cache={}
value=[]
def findPerm(n):
    #[1] - [1]
    #[1,2]-[1,2],[2,1]
    #[1,2,3]-
    k= len(n) #3 2 1
    single=[n[-1]] #3 2 1
    if k == 0: 
        return 0
    elif k==1:
        return [n]
    last=findPerm(n[:-1]) # [1,2]  [1]        
    print("last",[last])
    perms = []
    for s in last:
        for j in range(len(n)):
            perms.append(s[:j] + single + s[j:])
    return perms
def generate_permutations(A):
    if len(A) <= 1:
        return [A]
    first = A[-1]
    result = generate_permutations(A[:-1])
    permutations = []
    for p in result:
        for i in range(len(A)):
            left = p[:i]
            right = p[i:]
            permutations.append(left + [first] + right)
    return permutations

def helper(n):
    print(findPerm(n))
    #print(generate_permutations(n))
helper(n)

