#coding:utf-8
# 文本生成器

def lines(file):
    for line in file:yield line
    yield '\n'

def blocks(files):
    block = [];
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
