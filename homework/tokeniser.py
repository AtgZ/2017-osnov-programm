import sys
text = sys.stdin.read()
for i in ',:;?!.—)':
	text = text.replace(i, ' '+i)
for i in '(—.:?! ':
	text = text.replace(i, i+' ')
for i in '1234567890': 
	for j in '1234567890':
		text = text.replace(i + ' ' + j, i + j)	
row = text.split(' ')


token_id = 1
for token in row:
	token= token.strip()
	if token!='':
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (token_id, token))
	token_id=token_id+1