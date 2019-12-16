
def  same_ord(a, b): 
    
    while(a>1 and b>1):
    
        a=a/10
        b=b/10
    
    print(a,b)
    if(int(a)==int(b)):
        return True
    else:
        return False


print(same_ord(50, 700)) 

