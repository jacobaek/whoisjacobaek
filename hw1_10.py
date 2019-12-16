def factor(n):
	f=[]
	for i in range(2,n):
		if(n%i==0):
			f.append(i)
            
	return sum(f)+1
def amc(n):
    i=n+1
    while(True):
        
        f=factor(i)
        if(i==factor(f)):
            if(i!=f):
                return i
        i+=1

print(amc(5))
print(amc(220))
print(amc(284))
