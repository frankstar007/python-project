//文本生成器
def lines(file):
    for line in file:
        yield line
    yield '\n'
