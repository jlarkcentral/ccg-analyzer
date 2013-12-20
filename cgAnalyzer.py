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
	S = sys.argv[2].split(' ')

	A = PG.AGraph(directed=True)

	lex = []
	with open(sys.argv[1]) as f:
		for line in f:
			rule = line.split('\t')
			if len(rule) == 2:
				lex.append([rule[0],ruleParser.parse(rule[1])])
	
	tree = []
	tab = []
	nodi = 0
	nodiTab = []
	for i in range(len(S)):
		for r in lex:
			if r[0] == S[i]:
				tab.append(r[1])
				# drawing...
				A.add_node(nodi,label=str(r[0]))
				nodi += 1
	tree.append(tab)
	nodiTab.append(range(len(S)))

	for i in range(len(S)):
		for r in lex:
			if r[0] == S[i]:
				A.add_node(nodi,label=str(r[1]))
				nodi += 1
				A.add_edge(i,nodi-1)
	nodiTab.append(range(len(S),2*len(S)))
	print(tab)

	it = 0
	while it < len(S) and tree[-1] != ['S']:
		tab = []
		nodiInnerTab = []
		i = 0
		while i < len(tree[-1]):
			if i == len(tree[-1])-1:
				print('end of line')
				#print('\t'*i+ str(tree[-1][i]))
				tab.append(tree[-1][i])
				nodiInnerTab.append(nodiTab[-1][i])
			elif rule1(tree[-1][i],tree[-1][i+1]):
				print('rule1')
				#print(str(tree[-1][i][0]))
				tab.append(tree[-1][i][0])
				
				#drawing...
				A.add_node(nodi,label=str(tree[-1][i][0]))
				nodi += 1
				nodiInnerTab.append(nodi-1)
				A.add_edge(nodiTab[-1][i],nodi-1)
				print('add edge : ', str(nodiTab[-1][i]),str(nodi-1))
				A.add_edge(nodiTab[-1][i+1],nodi-1)
				print('add edge : ', str(nodiTab[-1][i+1]),str(nodi-1))
				i += 1
			elif rule2(tree[-1][i],tree[-1][i+1]):
				print('rule2')
				#print('\t'*i+ str(tree[-1][i+1][2]))
				tab.append(tree[-1][i+1][2])
				
				# drawing...
				A.add_node(nodi,label=str(tree[-1][i+1][2]))
				nodi += 1
				A.add_edge(nodiTab[-1][i],nodi-1)
				print('add edge : ', str(nodiTab[-1][i]),str(nodi-1))
				A.add_edge(nodiTab[-1][i+1],nodi-1)
				print('add edge : ', str(nodiTab[-1][i+1]),str(nodi-1))
				i += 1
			else:
				print('no rule')
				tab.append(tree[-1][i])
				nodiInnerTab.append(nodiTab[-1][i])

			i += 1
		nodiTab.append(nodiInnerTab)
		if tab != tree[-1]:
			tree.append(tab)
		else:
			break
		it += 1
		print(tab)

	if tree[-1] == ['S']:
		print("S in language")
		#print(prettyprint)
	else:
		print("S not in language")
	
	A.write('ademo.dot')
	A.layout(prog='dot')
	A.draw('graph.png')
	img = Image.open('graph.png')
	img.show()

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