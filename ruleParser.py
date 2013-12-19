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
	txt = '((SN\S)\\(N/N))/SN'
	print(parse(txt))

# parsing from text rule to list of symbols and operators
def parse(rule):
	symbols = nestedExpr('(',')').parseString('('+rule+')').asList()[0]
	print(symbols)
	r = []
	for e in symbols:
		r.append(parseList(e))
	print(r)
	return cleanSingleton(r,[])

# recursive nested brackets identification
def parseList(e):
	r = []
	if isinstance(e,list):
		for el in e:
			r.append(parseList(el))
	else:
		r.append(list(filter(('').__ne__,re.split('(\W)', e))))
		print(r)
	return r

def cleanSingleton(l,aux):
	for e in l:
		if isinstance(e,list) and len(e) == 1:
			while isinstance(e,list) and len(e) == 1:
				e = e[0]
		elif isinstance(e,list) and len(e) == 3:
			e = cleanSingleton(e,[])
		aux.append(e)
	return aux


if __name__ == '__main__':
	main()




