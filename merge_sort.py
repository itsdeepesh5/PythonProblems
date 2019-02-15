list1= [3, 4, 6, 10, 11, 15]
list2= [1, 5, 8, 12]

def merge_sort(list1, list2):

    #edge cases
    
    list1_index= list2_index =0

    merged_list = []
    
    while(list1_index < len(list1) and list2_index < len(list2)):
        if list1[list1_index] < list2[list2_index]:
            merged_list.append(list1[list1_index])
            list1_index+=1
        else:
            merged_list.append(list2[list2_index])
            list2_index+=1

    merged_list.extend(list1[list1_index:])
    merged_list.extend(list2[list2_index:])
    
    return merged_list

def partition(list):
    mid= len(list)/2
    return merge_sort(list[:mid], list[mid+1:])
    
print(partition(list1+list2))
