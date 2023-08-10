#Not work
n=int(input())
k=int(input())
#n=3
#k=10
kol=0
for i in range(k**(n-1),k**n):
	true=True
	for g in range(1,n-1):
		if((i%(k**g)==0) and (i%(k**(g+1))==0)):true=False;break
	if(true):kol+=1
print(kol)
