import sys
import re

table_sh = {'scia': 'ʃa',
'scio': 'ʃo',
'sciu': 'ʃu'}
table_sh_2 = {'sci': 'ʃi',
'sce': 'ʃe'}
table_k_gem = {'cca': 'kːa',
'cco': 'kːo',
'ccu': 'kːu',
'cche': 'kːe',
'cchi': 'k:i',
'ccia': 'tʃ:a',
'ccio': 'tʃ:o',
'cciò': 'tʃ:o',
'cciu': 'tʃ:u'}
table_k_gem_2 = {'cce': 'tʃ:e',
'cci': 'tʃ:i'}
table_k = {'ca': 'ka',
'co': 'ko',
'cu': 'ku',
'che': 'ke',
'chi': 'ki',
'cia': 'tʃa',
'cio': 'tʃo',
'ciò': 'tʃo',
'ciu': 'tʃu'}
table_k_2 = {'ce': 'tʃe',
'ci': 'tʃi'}


table_g_gem = {'gga': 'gːa',
'ggo': 'gːo',
'ggu': 'gːu',
'gghe': 'gːe',
'gghi': 'g:i',
'ggia': 'dʒ:a',
'ggio': 'dʒ:o',
'ggiu': 'dʒ:u'}
table_g_gem_2 = {'gge': 'dʒ:e',
'ggi': 'dʒ:i'}
table_g = {'ga': 'ga',
'go': 'go',
'gu': 'gu',
'ghe': 'ge',
'ghi': 'gi',
'gia': 'dʒa',
'gio': 'dʒo',
'giu': 'dʒu'}
table_g_2 = {'ge': 'dʒe',
'gi': 'dʒi'}

table_pal = {'gnia' : 'ɲ:a',
'gnio' : 'ɲ:o',
'gniu' : 'ɲ:u',
'glia' : 'ʎ:a',
'glio' : 'ʎ:o',
'gliu' : 'ʎ:u'}
table_pal_2 = {'gni' : 'ɲ:i',
'gne' : 'ɲ:e',
'gli' : 'ʎ:i',
'gle' : 'ʎ:e'}

table_q = {'qu': 'kw'}
table_gem = {'bb': 'b:',
'dd': 'd:',
'ff': 'f:',
'll': 'l:',
'mm': 'm:',
'nn': 'n:',
'pp': 'p:',
'rr': 'r:',
'ss': 's:',
'tt': 't:',
'vv': 'v:',
'x': 'ks',
'zz':'c:',
'z': 'c',
'h': ''}

table_diph = {'ia': 'ja',
'ie': 'je',
'iu': 'ju',
'io': 'jo',
'ua': 'wa',
'ue': 'we',
'uo': 'wo',
'ui': 'wi'}

table_s = {'s': 'z'}


#read through lines
for line in sys.stdin.readlines():
	line = line.lower()
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
	for c in table_sh:
		transliterated = transliterated.replace(c, table_sh[c])
	for c in table_sh_2:
		transliterated = transliterated.replace(c, table_sh_2[c])
	for c in table_k_gem:
		transliterated = transliterated.replace(c, table_k_gem[c])
	for c in table_k_gem_2:
		transliterated = transliterated.replace(c, table_k_gem_2[c])
	for c in table_k:
		transliterated = transliterated.replace(c, table_k[c])
	for c in table_k_2:
		transliterated = transliterated.replace(c, table_k_2[c])
	for c in table_g_gem:
		transliterated = transliterated.replace(c, table_g_gem[c])
	for c in table_g_gem_2:
		transliterated = transliterated.replace(c, table_g_gem_2[c])
	for c in table_g:
		transliterated = transliterated.replace(c, table_g[c])
	for c in table_g_2:
		transliterated = transliterated.replace(c, table_g_2[c])
	for c in table_pal:
		transliterated = transliterated.replace(c, table_pal[c])
	for c in table_pal_2:
		transliterated = transliterated.replace(c, table_pal_2[c])
	for c in table_q:
		transliterated = transliterated.replace(c, table_q[c])
	for c in table_gem:
		transliterated = transliterated.replace(c, table_gem[c])

#we can say that combinations like 'ia' are usually pronounced as a combination of a glide + vowel (e.g. piano) -- except short words (e.g. io). maybe there's a rule that you cannot have a glide in a monosyllabic word. 		
	for c in transliterated:
		if c in 'aeiou':
			vow = vow + 1
	if vow > 2:
		for c in table_diph:
			transliterated = transliterated.replace(c, table_diph[c])

#change s to z between vowels and before a voiced consonant
	for i in range (1, len(transliterated)-1):
		if transliterated[i] == 's' and transliterated[transliterated.index('s') - 1] in 'aeiou' and transliterated[transliterated.index('s') + 1] in 'aeioubdglmnr':
			transliterated = transliterated[:i]+'z'+transliterated[i+1:]
			continue
	if transliterated[0] == 's' and  transliterated[1] in 'bdglmnr':
			transliterated = 'z' + transliterated[1:]
	row[9] = 'Translit=' + transliterated
	print('\t'.join(row))
