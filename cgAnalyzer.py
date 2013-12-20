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
import ruleParser
import pygraphviz as PG
from PIL import Image


def main():
	
	S = ['Pierre','aime','les','pommes']

	A = PG.AGraph(directed=True, strict=True)

	A.add_edge("7th Edition", "32V")
	A.add_edge("7th Edition", "Xenix")
	# etc., etc.

	# save the graph in dot format
	A.write('ademo.dot')

	# pygraphviz renders graphs in neato by default, 
	# so you need to specify dot as the layout engine
	A.layout(prog='dot')
	
	A.draw('graph.png')

	img = Image.open('graph.png')
	img.show()

	'''
	lex = []
	with open(sys.argv[1]) as f:
		for line in f:
			rule = line.split('\t')
			if len(rule) == 2:
				lex.append([rule[0],ruleParser.parse(rule[1])])
	
	tree = []
	tab = []
	for i in range(len(S)):
		for r in lex:
			if r[0] == S[i]:
				tab.append(r[1])
	tree.append(tab)

	it = 0
	prettyprint = str(tab) + '\n\n'
	while it < len(S) and tree[-1] != ['S']:
		tab = []
		i = 0
		while i < len(tree[-1]):
			
			if i == len(tree[-1])-1:
				#print('end of line')
				#print('\t'*i+ str(tree[-1][i]))
				prettyprint += len(str(tree[-1][i]))*' ' + str(tree[-1][i]) + '\n\n'
				tab.append(tree[-1][i])
			elif rule1(tree[-1][i],tree[-1][i+1]):
				#print('rule1')
				#print(str(tree[-1][i][0]))
				prettyprint += len(str(tree[-1][i]))*' ' + str(tree[-1][i][0]) + '\n\n'
				tab.append(tree[-1][i][0])
				i += 1
			elif rule2(tree[-1][i],tree[-1][i+1]):
				#print('rule2')
				#print('\t'*i+ str(tree[-1][i+1][2]))
				prettyprint += len(str(tree[-1][i]))*' ' + str(tree[-1][i+1][2]) + '\n\n'
				tab.append(tree[-1][i+1][2])
				i += 1
			else:
				#print('no rule')
				#print(tree[-1][i])
				prettyprint += ' ' + str(tree[-1][i])
				tab.append(tree[-1][i])

			i += 1

		if tab != tree[-1]:
			tree.append(tab)
		else:
			break
		it += 1
		

	if tree[-1] == ['S']:
		print("S in language")
		print(prettyprint)
	else:
		print("S not in language")
	'''


def rule1(X,Y): # if A/B , B -> A
	#print(X,Y)
	if isinstance(X,list) and len(X) == 3 and X[1] == '/' and X[2] == Y:
		#print(X,Y)
		#print('---> ' + str(X[0]))
		return True
	else:
		return False

def rule2(X,Y): # if B , B\A -> A
	#print(X,Y)
	if isinstance(Y,list) and len(Y) == 3 and Y[1] == '\\' and Y[0] == X:
		#print(X,Y)
		#print('---> ' +str(Y[2]))
		return True
	else:
		return False

if __name__ == '__main__':
	main()