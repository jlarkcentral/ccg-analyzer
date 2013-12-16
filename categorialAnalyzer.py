#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

'''
Categorial grammar analyzer using CYK algorithm

usage:
python categorialAnalyzer.py <trainfile> <testfile>

author: j. lark
'''

import sys
from collections import defaultdict

def main():
	#let the input be a string S consisting of n characters: a1 ... an.
	S = ['Pierre','aime','les','voitures']
	#let the grammar contain r nonterminal symbols R1 ... Rr.
	g = []
	g.append(['Pierre','SN'])
	g.append(['aime','(SN\S)/SN'])
	g.append(['les','SN/N']) 
	g.append(['voitures','N'])
	#non_term = ['S','NP']

	P = defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:False)))

	for i in range(len(S)):
		for r in g:
			if r[0] == S[i]:
				P[i][1][r[0]] = True
				print(S[i])

	for i in range(2,len(S)+1):
		for j in range(len(S)-i+2):
			for k in range(i):
				for r in g:
					#print('P['+str(j)+']['+str(k)+']['+str(r[1][0])+'] = '+ str(P[j][k][r[1][0]]))
					#print('P['+str(j+k)+']['+str(i-k)+']['+str(r[1][1])+'] = '+ str(P[j+k][i-k][r[1][1]]))
					if P[j][k][r[1][0]] and P[j+k][i-k][r[1][1]]:
						P[j][i][r[0]] = True
						#print('---> P['+str(j)+']['+str(i)+']['+str(r)+'] = True')
					#print('===================')
	
	if P[0][len(S)]['S'] == True:
		print('S is in the language')

	else:
		print('S is NOT in the language')


if __name__ == '__main__':
	main()