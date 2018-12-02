from functools import partial

# 可迭代的对象，不断产生固定大小的内容块，直到文件结束
def a():
    record_size = 32
    with open('readme.md', 'r') as f:
        part = partial(f.read, record_size)
        for r in iter(part, ''):
            print(r)


a()
