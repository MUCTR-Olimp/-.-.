import sys
DICT=["adgjmpsvy. ","behknqtwz,","cfilorux!"]
if(False):file=sys.stdin
else:file=open("input.txt","r")
text=file.read()
if(text[-1]=="\n"):text=text[:-1]
output=0
for letter in text:output+=bool(DICT[0].find(letter)+1)*1+bool(DICT[1].find(letter)+1)*2+bool(DICT[2].find(letter)+1)*3
print(output)
