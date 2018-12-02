# 普通装饰器
def base_decorator(func):
    def based(*args, **kwargs):
        return func
    return based()


@base_decorator
def a():
    print('a12')


a()
