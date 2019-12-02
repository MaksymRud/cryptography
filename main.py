from time import sleep

from apa import apa
from math import gcd, ceil, sqrt
import random

li = []


def pollards_rho(n_):
    global li
    x = random.randint(2, n_ - 2)
    y = 1
    i = 0
    stage = 2
    while gcd(n_, abs(x - y)) == 1:
        if i == stage:
            y = x
            stage = stage * 2
        x = (x * x - 1) % n_
        i = i + 1
    p = gcd(n_, abs(x - y))
    # li.append(p)
    # return
    if p == 1:
        li.append(int(n_ / p))
        return
    if int(n_ / p) == 1:
        li.append(p)
        return
    if p > 3:
        pollards_rho(p)
    elif p <= 3:
        li.append(p)
    q = apa(n_)
    w = apa(p)
    d = q / w
    d = int(d[0])
    if d > 3:
        pollards_rho(d)
    elif d <= 3:
        li.append(d)


def bsgs(g, h, p):
    n = ceil(sqrt(p - 1))

    tbl = {str(pow(g, i, p)): i for i in range(1, n)}

    c = pow(g, (p - 2) * n, p)

    for j in range(1, n):
        d = h * pow(c, j, p)
        y = d % p
        if str(y) in tbl:
            return tbl[str(y)] + n * j

    return None


def EulerPhi(a):
    global li
    li = []
    pollards_rho(a)
    s = a
    k = []
    for d in li:
        if d not in k:
            s *= (1 - 1 / d)
            k.append(d)
    return s


def mobius(n):
    global li
    li = []
    pollards_rho(n)
    for x in li:
        if li.count(x) > 1:
            return 0
    if len(li) % 2 == 0:
        return 1
    else:
        return -1


def Legendre(a: int, p: int):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a % 2 == 0:
        result = Legendre(a // 2, p)
        if not (p * p - 1) & 8 == 0:
            result = -result
    else:
        result = Legendre(p % a, a)
        if ((a - 1) * (p - 1) & 4) != 0:
            result = -result
    return result


def calculateJacobi(a, p):
    s = 1
    pollards_rho(p)
    for d in li:
        s *= Legendre(a, d)
    return s


def cipolla(n, p):
    global li
    while True:
        a = random.randint(1, p - 1)
        l = Legendre((a ** 2 - n), p)
        if l == -1:
            break

    def bits(n_):
        while n_:
            yield n_ & 1
            n_ >>= 1

    def cipollaMult(a, b, c, d, w, p):
        return (a * c + b * d * w) % p, (a * d + b * c) % p

    x1 = (a, 1)
    x2 = cipollaMult(x1[0], x1[1], x1[0], x1[1], a * a - n, p)
    for i in bits(int((p + 1) / 2)):
        if i == 0:
            x2 = cipollaMult(x2[0], x2[1], x1[0], x1[1], a * a - n, p)
            x1 = cipollaMult(x1[0], x1[1], x1[0], x1[1], a * a - n, p)
        else:
            x1 = cipollaMult(x1[0], x1[1], x2[0], x2[1], a * a - n, p)
            x2 = cipollaMult(x2[0], x2[1], x2[0], x2[1], a * a - n, p)
    # if x1[0] ** 2 % p == n:
    return x1[0], -x1[0] % p
    # else:
    #     return cipolla(n, p)


def miller_rabin(n, k=10):
    if n % 2 == 0:
        return False

    s = 0
    t = n - 1
    while t % 2 == 0:
        t = t // 2
        s += 1

    for i in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        ok = False
        for j in range(s - 1):
            x = x ** 2 % n
            if x == 1:
                return False
            if x == n - 1:
                ok = True
                break
        if ok:
            continue
        else:
            return False
    return True


def elgamel(m, p, g):
    x = random.randint(2, p - 1)
    y = pow(g, x, p)
    k = pow(2, p - 2)
    a = pow(g, k, p)
    b = pow(y, k) * m % p
    return a, b, x


def decode_elgamel(a, b, x, p):
    m = b * pow(a, p - 1 - x) % p
    return m


# pollards_rho(17348256187264213649126346457)
# print(li)

# print(bsgs(3, 1, 196134577))
#
# print(pow(3, 24516822, 196134577))

# print(int(EulerPhi(9)))

# print(mobius(10))

# print(calculateJacobi(7, 15))

# print(cipolla(10, 13))

# print(Legendre(30, 97))

# print(miller_rabin(18446744082299486207, k=10))

# a_, b_, x_ = elgamel(5, 11, 2)
# print(a_, b_, x_)
# print(decode_elgamel(a_, b_, x_, 11))
