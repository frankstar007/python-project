#coding:utf-8
#测试文件
import sys
def lines(file):
    line_list = []
    for line in file(sys.stdin):
        line_list.append(line);
    line_list.append('\n')
    return line_list;
