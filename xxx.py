x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x[::2] = "ABCDE"

def foo(x, y, z=None):
    pass

def bar(*args, zap=None, **kwargs):
    print(zap)
    foo(*args, **kwargs)