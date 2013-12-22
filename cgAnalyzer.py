#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

'''
Categorial grammar analyzer using pseudo-CYK algorithm

usage:
python categorialAnalyzer.py <rule file> "string sample" [-g]

author: j. lark
'''

import sys
import ruleParser
import pygraphviz as PG
from PIL import Image


def main():
	if len(sys.argv) > 4 or len(sys.argv) < 3:
		print('usage: \n python cgAnalyzer.py <lexicon file> "string sample" [-g]')
		exit()

	# input sentence
	S = sys.argv[2].split(' ')

	# lexicon initialization
	lex = []
	with open(sys.argv[1]) as f:
		for line in f:
			rule = line.split('\t')
			if len(rule) == 2:
				lex.append([rule[0],ruleParser.parse(rule[1])])


	lexParts = getLexParts(S,lex)
	for lp in lexParts:
		analyze(S,lp)


# sentence analysis
def analyze(S,lex):
	# graph initialization
	A = PG.AGraph(directed=True)

	# array initialization
	tree = []
	tab = []
	nodi = 0
	nodiTab = []
	for r in lex:
		tab.append(r[1])
		# drawing...
		A.add_node(nodi,label=r[0])
		nodi += 1
	tree.append(tab)
	nodiTab.append(range(len(S)))

	i = 0
	for r in lex:
		A.add_node(nodi,label=ruleParser.labelize(r[1]))
		nodi += 1
		A.add_edge(i,nodi-1)
		i += 1
	nodiTab.append(range(len(S),2*len(S)))



	# main algorithm
	it = 0
	while it < len(S) and tree[-1] != ['S']:
		tab = []
		nodiInnerTab = []
		i = 0
		while i < len(tree[-1]):
			if i == len(tree[-1])-1: # end of list
				tab.append(tree[-1][i])
				nodiInnerTab.append(nodiTab[-1][i])

			elif rule1(tree[-1][i],tree[-1][i+1]): # rule 1 applies
				tab.append(tree[-1][i][0])
				
				#drawing...
				A.add_node(nodi,label=ruleParser.labelize(tree[-1][i][0]))
				nodi += 1
				nodiInnerTab.append(nodi-1)
				A.add_edge(nodiTab[-1][i],nodi-1)
				A.add_edge(nodiTab[-1][i+1],nodi-1)
				i += 1
			
			elif rule2(tree[-1][i],tree[-1][i+1]): # rule 2 applies
				tab.append(tree[-1][i+1][2])
				
				# drawing...
				A.add_node(nodi,label=ruleParser.labelize(tree[-1][i+1][2]))
				nodi += 1
				nodiInnerTab.append(nodi-1)
				A.add_edge(nodiTab[-1][i],nodi-1)
				A.add_edge(nodiTab[-1][i+1],nodi-1)
				i += 1

			else: # no rule
				tab.append(tree[-1][i])
				
				# drawing...
				nodiInnerTab.append(nodiTab[-1][i])
			i += 1
		nodiTab.append(nodiInnerTab)
		if tab != tree[-1]:
			tree.append(tab)
		else:
			break
		it += 1





	# result
	pp = ''
	for i in range(len(S)):
		pp += S[i]+' ---> '+ruleParser.labelize(lex[i][1])+'\n'

	if tree[-1] == ['S']:
		print('\''+" ".join(S)+'\', using:\n\n'+pp+'\nis recognized')
		print('==============================')
		n=A.get_node(nodiTab[-1][-1])
		A.node_attr['style']='filled'
		n.attr['fillcolor']='green'
	else:
		print(" ".join(S)+', using:\n\n'+pp+'\nis not recognized')
		print('==============================')

	if len(sys.argv) == 4 and sys.argv[3] =='-g':
		A.layout(prog='dot')
		A.draw('graph.png')
		img = Image.open('graph.png')
		img.show()


# if A/B , B -> A
def rule1(X,Y):
	return isinstance(X,list) and len(X) == 3 and X[1] == '/' and X[2] == Y

# if B , B\A -> A
def rule2(X,Y):
	return isinstance(Y,list) and len(Y) == 3 and Y[1] == '\\' and Y[0] == X

def getLexUsed(s,l):
	lexUsed = []
	for w in s:
		for e in l:
			if e[0] == w:
				lexUsed.append(e)
	return lexUsed


# get all analyzable lexicon versions
def getLexParts(s,l):
	lexUsed = getLexUsed(s,l)
	lexParts = []
	lexPart = []
	lexParts.append(lexPart)
	for i in range(len(lexUsed)):
		if i > 0 and lexUsed[i-1][0] == lexUsed[i][0]:
			lpsCopy = lexParts[:]
			for lp in lpsCopy:
				newLp = lp[:-1]
				newLp.append(lexUsed[i])
				lexParts.append(newLp)
		else:
			for lp in lexParts:
				lp.append(lexUsed[i])
	return lexParts
	


if __name__ == '__main__':
	main()