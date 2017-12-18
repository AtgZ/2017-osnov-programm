import sys
import re

table_1 = {'а': 'a',
'б': 'b',
'в': 'v',
'г': 'g',
'д': 'd',
'е': 'je',
'ё': 'jo',
'ж': 'zh',
'ӝ': 'dzh',
'з': 'z',
'ӟ': 'dz\'',
'и': 'ji',
'ӥ': 'i',
'й': 'j',
'к': 'k',
'л': 'l',
'м': 'm',
'н': 'n',
'о': 'o',
'ӧ': 'e̯',
'п': 'p',
'р': 'r',
'с': 's',
'т': 't',
'у': 'u',
'ф': 'f',
'х': 'x',
'ц': 'ts',
'ч': 'ch\'',
'ӵ': 'ch',
'ш': 'sh',
'щ': 'shch',
'ъ': '$',
'ы': 'i̯',
'э': 'e',
'ю': 'ju',
'я': 'ja'}
table_j = {'j': '\''}

table_pal = {'ь' : '\'', 
'$': ''}



#read through lines
for line in sys.stdin.readlines():
	line = line.strip('\n') 
	if line == '':
		print()
		continue
	if line [0] == '#':
		print(line)
		continue
	row = line.split('\t')
	transliterated = row[1]
	vow = 0
	for c in table_1:
		transliterated = transliterated.replace(c, table_1[c])
	if 'j' in transliterated:
		if transliterated[transliterated.index('j') - 1] in 'bdfghklmnprstfxc':
			for c in table_j:
				transliterated = transliterated.replace(c, table_j[c])
	for c in table_pal:
		transliterated = transliterated.replace(c, table_pal[c])

	row[7] = 'Translit=' + transliterated
	print('\t'.join(row))
