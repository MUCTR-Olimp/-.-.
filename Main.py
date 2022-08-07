import sys
if(False):file=sys.stdin
else:file=open("input.txt","r")
text=str(file.read())
file.close()
QXX,ZZZ=list(map(int,text[:text.find("\n")].split()))
ZZZ-=sum(list(map(int,text[text.find("\n"):].split())))*20
if(ZZZ<QXX):print("Dirty debug :(")
else:print("No chance.")

