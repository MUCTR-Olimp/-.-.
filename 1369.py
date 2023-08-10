#Not work
from threading import Thread
Havchik=[]
Havchikforhavchik=[]
outputindex=0
def DoIt(x,y,ind):
	global outputindex
	output=""
	mi=(Havchik[0][0]-x)**2+(Havchik[0][1]-y)**2
	for indextar in range(M):
		if(Havchik[indextar][0]-x+Havchik[indextar][1]-y>mi):continue
		aaaa=(Havchik[indextar][0]-x)**2+(Havchik[indextar][1]-y)**2
		if(aaaa==mi):output+=str(indextar+1)+" "
		elif(aaaa<mi):output=str(indextar+1)+" ";mi=aaaa
	while(outputindex!=ind):pass
	print(output);outputindex+=1
M=int(input())
for i in range(M):Havchik.append(list(map(float,input().split())))
N=int(input())
pool=[]
for i in range(N):
	x,y=list(map(int,input().split()))
	pool.append(Thread(target=DoIt,args=(x,y,i,),daemon=True))
for i in range(N):pool[i].start()
for g in range(N):pool[g].join()
