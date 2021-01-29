# def get_sum(a, b, c=0, d=0):
#     return a + b + c + d
# print(get_sum(1, 2, d=12))

# def get_num(*args):
#     return sum(args)
#
# print(get_num(1, 2, 3, 4, 8))


# def func(**kwargs):
#     return (kwargs)
#
# print(func(test=1, test2=3, simple_num=4, string=5))


def f(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)

f(1, 2, 3, 4, b='test', c='Hi')
