import random
from math import sqrt


def double(x, y):
    m = (3 * x ** 2 + a) * (2 * y) ** (p - 2) % p

    xx = (m ** 2 - 2 * x) % p

    return xx, -(y + m * (xx - x)) % p


def add(x1, y1, x2, y2):
    m = (y1 - y2) * (x1 - x2) ** (p - 2) % p

    xx = (m ** 2 - x1 - x2) % p

    return xx, -(y1 + m * (xx - x1)) % p


def bits(n):
    while n:
        yield n & 1
        n >>= 1


def double_and_add(n, x, y):
    st = 1
    x__, y__ = 0, 0

    for bit in bits(n):
        if bit == 1:
            if x__ == 0 and y__ == 0:
                x__, y__ = x, y
            else:
                x__, y__ = add(x__, y__, x, y)
        st *= 2
        x, y = double(x, y)

    return x__, y__


p = 224737
a = int('DB7C2ABF62E35E668076BEAD2088', base=16)
b = int('659EF8BA043916EEDE8911702B22', base=16)
x_ = random.randint(1, p - 1)
y_ = int(sqrt(x_ ** 3 + a * x_ + b)) % p
a_ = random.randint(3, 20)
beta = double_and_add(a_, x_, y_)

print("open - alpha ({}, {}) and beta ({}, {})".format(x_, y_, beta[0], beta[1]))
print("secret - {}".format(a_))

m = int(input("message: "))
m1, m2 = m, m
k = random.randint(2, 10)
y1_ = double_and_add(k, x_, y_)
q = double_and_add(k, beta[0], beta[1])
y2_ = add(m1, m2, q[0], q[1])
print("sending y1 ({}, {}) and y2 ({}, {})".format(y1_[0], y1_[1], y2_[0], y2_[1]))


q = double_and_add(a_, y1_[0], y1_[1])
m = add(y2_[0], y2_[1], q[0], -q[1])
print("received - {}".format(m[0]))

# print(add(2, -2, 1, -2))
# print(double_and_add(5, 3, 6))
# print(double(3, 6))
