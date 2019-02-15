num=[['A'],['B',['C']],['D','E',['F','G']]]
a=[]
def flatten(num):
    for i in num:
        print(i)
        if isinstance(i, list):
            print('sending', i)
            flatten(i)
        else:
            a.extend(i)
    return a


print(flatten(num))


 
