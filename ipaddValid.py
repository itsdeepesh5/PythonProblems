nums="0.0.0.0/0"
def isipValid(nums):
    if len(nums)==0:
        return False

    if len(nums.split(".")) > 4:
        return False
    try: 
        i=0
        for num in nums.split("."):
            if i==3:
                n1= num.split("/")
                if len(n1)> 2:
                    return False
                if (int(n1[0])<0 and int(n1[0]) > 255) :
                    return False
                if not n1[1].isNumeric() :
                    return False
                
            if int(num) > 255 and int(num) < 0 :
                return False
    except:
        return False

    return True

print(isipValid(nums))
        
    
