def get_sum(a, b):
    """
    Returns sum of arguments a & b.

    :param a: First Operand
    :type a: int
    :param b: Second Operand
    :type b: int
    :return: Return type int
    """
    return a + b


# print(get_sum(1, 1))

a = 5  # Global variables available for read-only

#
#
# def f():
#     a = 20
#     a += 1
#     print(a)
#
#
# print(a)
# f()
# print(a)


# def f():
#     global a
#     a += 1
#     print(a )
#
#
# print(a)
# f()
# print(a)


l = [1, 'dkjfhd', 3]

def f(l):
    return [elem * 2 for elem in l]

print(f(l))


def f2(l):
    def get_mult(x):
        return x * 2
    return [get_mult(i) for i in l]

print(f2(l))


def f3(l):
    def get_mult(x):
        if isinstance(x, int):
            return x * 2
    return [get_mult(i) for i in l if get_mult(i)]

print(f3(l))


def f4(l):
    def get_mult(x):
        return x * 2
    return list(map(get_mult, l))

print(f4(l))