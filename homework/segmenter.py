import sys
text = sys.stdin.read()
for i in '!.?':
	text = text.replace(i+' ', i+'\n')
print (text)