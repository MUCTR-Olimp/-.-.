#Success
import sys
if(True):file=sys.stdin
else:file=open("input.txt","r")
n,m=list(map(int,file.read().split()))
file.close()
if((m==1) and (n!=1)):print(1)
elif(n==1):print(0)
else:print((min(n,m)-1)*2+int(m<n))
