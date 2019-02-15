str="this is my Sentense.. this is mY sentense"

def countwords(str):
    start=0
    length=0
    result= []
    
    if len(str) ==0:
        return str
    
    for i, char in enumerate(str):
        if char == " ":
            if length > 0 and str[start:start+length].lower() not in result:
                result.append(str[start:start+length].lower())
            start= i+1
            length=0
        elif char == "." and i >= 0:
            if length > 0:
                if str[start:start+length].lower() not in result:
                    result.append(str[start:start+length].lower())
                length=0
                start= i+1
                
            else:
                start=i+1
                length=0
        elif char.isalpha():
            length+=1
 
    return len(result)

print(countwords(str))
