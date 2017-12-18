import sys

tokens = []
all_tokens = []
tags = ['ADJ', 'ADV', 'INTJ', 'NOUN', 'PROPN', 'VERB', 'ADP', 'AUX', 'CCONJ', 'DET', 'NUM', 'PART', 'PRON', 'SCONJ', 'PUNCT', 'SYM', 'X']



text = sys.stdin.readlines()
for line in text:
	row = line.split('\t')
	all_tokens.append(row[1])
	if row[1] not in tokens:
		tokens.append(row[1])
	if row[3] not in tags:
		tags.append(row[3])
print('This is the list of tokens: \n', tokens)
print('These are the tags used: \n', tags)
	
m = {}

for w1 in tokens: 
	if w1 not in m: 
		m[w1] = {}
	for w2 in tags:
		m[w1][w2] = 0

tag_fr = {}
lem_fr = {}

for w1 in tags:
	tag_fr[w1] = 0
for w1 in tokens:
	lem_fr[w1] = 0

nonzero_tags = {}
for w1 in tokens:
	nonzero_tags[w1] = []

num_lin = 0

for line in text:
	row = line.split('\t')
	w1 = row[1]
	w2 = row[3]
	m[w1][w2] = m[w1][w2] + 1
	lem_fr[w1] += 1
	tag_fr[w2] += 1
	num_lin += 1
	if row[3] not in nonzero_tags[w1]:
		nonzero_tags[w1].append(row[3])
 


tag_pr = {}

for w1 in tags:
	tag_pr[w1] = tag_fr[w1]/len(all_tokens)


pr = {}
for w1 in tokens:
	if w1 not in pr: 
		pr[w1] = {}
	for w2 in tags:
		pr[w1][w2] = m[w1][w2]/lem_fr[w1]


print('P\tcounts\ttag\tform')
for tag in tags:
	print('%f\t%d\t%s\t_' % (tag_pr[tag], tag_fr[tag], tag))
for token in tokens:
	for nz in nonzero_tags[token]:
		print ('%f\t%d\t%s\t%s' % (pr[token][nz], m[token][nz], nonzero_tags[token][nonzero_tags[token].index(nz)], token))