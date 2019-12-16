
def  double_5(n):
     
    while(n//10!=0):
        a=n%10
        n=n//10
        b=n%10
        if(a==b):
            break
    if(a==b):
        return True
    else:
        return False
        
    
    



print( double_5 (50505050) ) 

print( double_5 (1055000) ) 