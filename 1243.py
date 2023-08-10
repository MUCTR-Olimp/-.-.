#Success
import sys
if(True):file=sys.stdin
else:file=open("input.txt","r")
output=int(file.read())
print(output%7)
