#Success
import sys
if(True):file=sys.stdin
else:file=open("input.txt","r")
Petr,Petr_delta,Taks,Taks_delta=list(map(int,file.read().split()))
file.close()
if(Taks<=Petr):print(Petr)
else:
	while(True):
		if(Petr+Petr_delta>=Taks):print(Taks);break
		Petr+=Petr_delta
		if(Taks-Taks_delta<=Petr):print(Petr);break
		Taks-=Taks_delta
