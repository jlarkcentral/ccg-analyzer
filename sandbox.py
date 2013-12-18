#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

import re

def main():
	txt = '(SN\S)/(SN/N)\\N'
	print(parse(txt))

def parse(txt):
	symbols = list(filter(('').__ne__, re.split('(\W)', txt)))
	r = []
	for s in symbols:
		
	return r

if __name__ == '__main__':
	main()