#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

'''
Rule parsing for ccg-analyzer

author: j.lark
'''

import re
from pyparsing import nestedExpr
import itertools

def main():
	txt = '(SN\S)\\(N/N)'
	print(parse(txt))

# parsing from text rule to list of symbols and operators
def parse(rule):
	symbols = nestedExpr('(',')').parseString('('+rule+')').asList()[0]
	print(symbols)
	r = []
	for e in symbols:
		r.append(parseList(e))
	return r

# recursive nested brackets identification
def parseList(e):
	r = []
	if isinstance(e,list):
		for el in e:
			r.append(parseList(el))
	else:
		r.append(list(filter(('').__ne__,re.split('(\W)', e))))
		print(r)
	for e in r:

	return r

def cleanSingleton(l):
	r = []
	for e in l:
		if 

if __name__ == '__main__':
	main()




'''
CYK

def main():
	#let the input be a string S consisting of n characters: a1 ... an.
	S = ['le','bateau','rouge','coule']
	#let the grammar contain r nonterminal symbols R1 ... Rr.
	g = []
	g.append(['S',['NP','V']])
	g.append(['NP',['DET','N']])
	g.append(['NP',['NP','ADJ']]) 
	g.append(['DET','le'])
	g.append(['ADJ','rouge'])
	g.append(['N','bateau'])
	g.append(['V','coule'])
	non_term = ['S','NP']

	P = defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:False)))

	for i in range(len(S)):
		for r in g:
			if r[1] == S[i]:
				P[i][1][r[0]] = True
				print(S[i])

	for i in range(2,len(S)+1):
		for j in range(len(S)-i+2):
			for k in range(i):
				for r in g:
					if r[0] in non_term:
						print('P['+str(j)+']['+str(k)+']['+str(r[1][0])+'] = '+ str(P[j][k][r[1][0]]))
						print('P['+str(j+k)+']['+str(i-k)+']['+str(r[1][1])+'] = '+ str(P[j+k][i-k][r[1][1]]))
						if P[j][k][r[1][0]] and P[j+k][i-k][r[1][1]]:
							P[j][i][r[0]] = True
							print('---> P['+str(j)+']['+str(i)+']['+str(r)+'] = True')
						print('===================')
	
	if P[0][len(S)]['S'] == True:
		print('S is in the language')
	else:
		print('S is NOT in the language')
'''
