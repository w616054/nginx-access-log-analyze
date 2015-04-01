#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: 
# Revision: 0.0
# Date: 2015-03-27
# Auth: wangliang
########

import sys
import json


def my_handle(lines, num):
	list_n = []
	for one in xrange(len(lines)):
		list_n.append(lines[one].split()[num].strip("\""))

	return list_n

def my_count(my_list):
	# 排序
	tmp_list = list(set(my_list))
	# 去重 
	tmp_list.sort()
	
	dic = {}
	for one in tmp_list:
		dic[one] = my_list.count(one)

	return dic


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Usage: python %s logfile"  % sys.argv[0]
		sys.exit(0)

	# 打开日志文件
	f = open(sys.argv[1], 'r')
	lines = f.readlines()
	f.close()

	# 各字段修改相应的数字即可
	# 每行按空格分割，数字对应各个字段
	# 不同的日志格式，数字会不同
	_list = my_handle(lines, 0)
	print json.dumps(my_count(_list), sort_keys=True, indent=4)

	_list = my_handle(lines, 5)
	print json.dumps(my_count(_list), sort_keys=True, indent=4)

