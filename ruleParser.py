#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

'''
Rule parsing for cg-analyzer

author: j.lark
'''

import re
from pyparsing import nestedExpr

# parsing from text rule to list of symbols and operators
def parse(rule):
	symbols = nestedExpr('(',')').parseString('('+rule+')').asList()[0]
	r = []
	for e in symbols:
		newParse = parseList(e)
		if len(newParse) == 1:
			r.append(newParse[0])
		elif len(newParse) == 2:
				r.append(newParse[0])
				r.append(newParse[1])
		else:
			r.append(newParse)
	while isinstance(r,list) and len(r) == 1:
		r = r[0]
	return r

# recursive nested brackets identification
def parseList(e):
	r = []
	if isinstance(e,list):
		for el in e:
			newParse = parseList(el)
			if len(newParse) == 1:
				r.append(newParse[0])
			elif len(newParse) == 2:
				r.append(newParse[0])
				r.append(newParse[1])
			else:
				r.append(newParse)
	else:
		split = list(filter(('').__ne__,re.split('(\W)', e)))
		for el in split:
			r.append(el)
	return r

# list of symbols into label
def labelize(l):
	r = ''
	for e in l:
		if isinstance(e,list):
			r += '('+labelize(e)+')'
		else:
			r += e.replace('\\','\\\\')
	return r
