#Not work
def CheckSimple(n):
  if(n%2==0):return n==2
  d=3
  while(d*d<=n):
		if(n%d==0):return False
		d+=2
	return True
#n=4
n=int(input())
ind=[]
#ind=[3,2,5,7]
for i in range(n):ind.append(int(input()))
n=max(ind)
i=2
k=0
out=[]
while(k<n):
	if(CheckSimple(i)):
		#print(i)
		k+=1
		if(k in ind):out.append((ind.index(k),str(i)))
		#for g in range(len(ind)):
		#	if(ind[g]==k):out.append(str(i));break
	i+=1
for i in range(len(ind)):
	for g in range(len(ind)):
		if(i==out[g][0]):break
	print(out[g][1])
