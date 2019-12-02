import math


class Number:
    def __init__(self, value):
        value = str(value)
        self.value = value

    @property
    def value(self):
        if self.sign == '-':
            return '-' + self.s
        return self.s

    @value.setter
    def value(self, value: str):
        self.s = value
        self.digit = []  # digits of a value
        if value[0] == '-':
            self.sign = '-'
            self.s = self.s[1:]
        else:
            self.sign = '+'
        for i in range(len(self.s)):
            self.digit.append(int(self.s[i]))
        Number.remove_leading_zeros(self)

    def __add__(self, other):
        """
        adding method for apa
        :param other:
        :return: Number - result of adding
        """
        other = Number.to_number(other)
        if self.sign == '-' and other.sign == '+':
            return other._sub(self)
        if self.sign == '+' and other.sign == '-':
            return self._sub(other)
        if self.sign == '+' and other.sign == '+':
            return self._add(other)
        if self.sign == '-' and other.sign == '-':
            n = self._add(other)
            n.change_sign()
            return n

    def __sub__(self, other):
        other = Number.to_number(other)
        if self.sign == '-' and other.sign == '-':
            return other._sub(self)
        if self.sign == '+' and other.sign == '-':
            return other._add(self)
        if self.sign == '-' and other.sign == '+':
            n = other._add(self)
            n.change_sign()
            return n
        if self.sign == '+' and other.sign == '+':
            return self._sub(other)

    def __mul__(self, other):
        other = Number.to_number(other)
        n = self._mul(other)
        if not self.sign == other.sign:
            n.change_sign()
        return n

    def __truediv__(self, other):
        other = Number.to_number(other)
        if self.sign == '+' and other.sign == '+':
            return self._div(other)
        elif self.sign == '-' and other.sign == '-':
            return self._div(other)
        elif self.sign == '+' and other.sign == '-':
            n, m = self._div(other)
            Number.change_sign(n)
            return n, m
        elif self.sign == '-' and other.sign == '+':
            n, m = self._div(other)
            if Number('-1') * n * other > self:
                Number.change_sign(n)
                n -= 1
                m = self - n * other
                return n, m
            Number.change_sign(n)
            return n, m

    def __pow__(self, power, modulo=None):
        power = Number.to_number(power)
        return self._pow(power)

    def _add(self, other):
        rez = []
        # remembering bigger number and the length of smaller
        if len(self.digit) > len(other.digit):
            length = len(other.digit)
            bigger = self
        elif len(self.digit) < len(other.digit):
            length = len(self.digit)
            bigger = other
        else:
            length = len(self.digit)
            bigger = None
        d = 0
        i = 0
        # adding digits while smaller
        while not i == length:
            i = i + 1
            rez.append((self.digit[len(self.digit) - i] + other.digit[len(other.digit) - i] + d) % 10)
            d = (self.digit[len(self.digit) - i] + other.digit[len(other.digit) - i] + d) // 10
        # appending the part of bigger one
        if bigger is not None:
            while not i == len(bigger.digit):
                i = i + 1
                rez.append((bigger.digit[len(bigger.digit) - i] + d) % 10)
                d = (bigger.digit[len(bigger.digit) - i] + d) // 10
        if d == 1:
            rez.append(1)
        rez.reverse()
        n = Number(Number.to_string(rez))
        return n

    def _sub(self, other):
        rez = []
        # remembering bigger number and the length of smaller
        if abs(self) > abs(other):
            length = len(other.digit)
            bigger = self
            smaller = other
            sign = '+'
        elif abs(self) < abs(other):
            length = len(self.digit)
            bigger = other
            smaller = self
            sign = '-'
        else:
            return Number('0')
        d = 0
        i = 0
        # adding digits while smaller
        while not i == length:
            i = i + 1
            c = bigger.digit[len(bigger.digit) - i] - smaller.digit[len(smaller.digit) - i] - d
            if c < 0:
                c = c + 10
                d = 1
            else:
                d = 0
            rez.append(c)
        # appending the part of bigger one
        while not i == len(bigger.digit):
            i = i + 1
            c = bigger.digit[len(bigger.digit) - i] - d
            if c < 0:
                d = 1
                c = c + 10
            else:
                d = 0
            rez.append(c)
        rez.reverse()
        n = Number(Number.to_string(rez))
        n.sign = sign
        return n

    def _mul(self, other):
        if len(self.digit) > len(other.digit):
            smaller = other
            bigger = self
        else:
            smaller = self
            bigger = other
        number = Number('0')
        for i in range(len(smaller) - 1, -1, -1):
            n = ''
            d = 0
            for j in range(len(bigger) - 1, -1, -1):
                n = str((smaller[i] * bigger[j] + d) % 10) + n
                d = (smaller[i] * bigger[j] + d) // 10
            if not d == 0:
                n = str(d) + n
            number += Number(n + '0' * (len(smaller) - i - 1))
        return number

    def _div(self, other):
        other = Number(other)
        if other == 0:
            return ValueError('You can\'t dive on 0')
        if self == 0:
            return Number('0'), Number('0')
        i = 0
        a = '0'
        ans = ''
        skip = False
        a_n = Number(a)
        while i < len(self):
            if not skip:
                a += str(self[i])
            a_n = Number(a)
            if a_n < other:
                ans += '0'
                i += 1
                skip = False
            else:
                for j in range(0, 10):
                    if other * (j + 1) > a_n:
                        ans += str(j)
                        a_n -= other * j
                        i += 1
                        if i < len(self):
                            a = str(a_n) + str(self[i])
                            skip = True
                        break
        return Number(ans), a_n

    def _pow(self, b):
        if b == 0:
            return 1

        r = 1
        num = Number(str(self))

        def bits(n):
            while n:
                yield n & 1
                n >>= 1

        for bit in bits(int(b)):
            if bit == 1:
                r = num * r
            num = num * num
        return r

    def __lt__(self, other):
        """
        self < other
        :param other:
        :return:
        """
        other = Number.to_number(other)
        if self.sign == '-' and other.sign == '+':
            return True
        elif self.sign == '+' and other.sign == '-':
            return False
        elif self.sign == '+' and other.sign == '+':
            if len(self) > len(other):
                return False
            elif len(self) < len(other):
                return True
            for i in range(len(self)):
                if self.digit[i] < other.digit[i]:
                    return True
                elif self.digit[i] > other.digit[i]:
                    return False
        elif self.sign == '-' and other.sign == '-':
            if len(self) > len(other):
                return True
            elif len(self) < len(other):
                return False
            for i in range(len(self)):
                if self.digit[i] > other.digit[i]:
                    return True
                elif self.digit[i] < other.digit[i]:
                    return False
        return False

    def __gt__(self, other):
        n = Number.to_number(other)
        return n.__lt__(self)

    def __eq__(self, other):
        other = Number.to_number(other)
        if not self.sign == other.sign or not len(self) == len(other):
            return False
        for i in range(len(self)):
            if not self.digit[i] == other.digit[i]:
                return False
        return True

    def __ge__(self, other):
        other = Number.to_number(other)
        if self.__gt__(other) or self.__eq__(other):
            return True
        else:
            return False

    def __le__(self, other):
        other = Number.to_number(other)
        return other.__ge__(self)

    @staticmethod
    def sum(first, second, mode=None):
        first = Number.to_number(first)
        if mode is None:
            return first.__add__(second)
        mode = Number.to_number(mode)
        return first.__add__(second).__mod__(mode)

    @staticmethod
    def sub(first, second, mode=None):
        first = Number.to_number(first)
        if mode is None:
            return first.__sub__(second)
        mode = Number.to_number(mode)
        s = first.__sub__(second)
        return s + mode if s < 0 else s

    @staticmethod
    def mul(first, second, mode=None):
        first = Number.to_number(first)
        if mode is None:
            return first.__mul__(second)
        mode = Number.to_number(mode)
        d = first.__mul__(second)
        n, m = d.__truediv__(mode)
        return d - n * mode

    @staticmethod
    def div(first, second, mode=None):
        first = Number.to_number(first)
        if mode is None:
            n, m = first.__truediv__(second)
            return
        mode = Number.to_number(mode)
        second = Number.to_number(second)
        n, m = first.__truediv__(second)
        return n.__mod__(mode)
        # x1, x2, x3 = Number('1'), Number('0'), mode
        # y1, y2, y3 = Number('0'), Number('1'), second
        # while True:
        #     if y3 == 0:
        #         return Number('-0')
        #     if y3 == 1:
        #         y2 = y2 if y2 > 0 else y2 + mode
        #         n = first.__mul__(y2)
        #         n = n.__mod__(mode)
        #         return n
        #     g, m = x3.__truediv__(y3)
        #     t1, t2, t3 = x1 - g.__mul__(y1), x2 - g.__mul__(y2), x3 - g.__mul__(y3)
        #     x1, x2, x3 = y1, y2, y3
        #     y1, y2, y3 = t1, t2, t3

    @staticmethod
    def pow(first, second, mode=None):
        first = Number.to_number(first)
        second = Number.to_number(second)
        if mode is None:
            return first.__pow__(second)
        mode = Number.to_number(mode)
        p = first.__pow__(second)
        return Number.to_number(p).__mod__(mode)

    def change_sign(self):
        if self.sign == '-':
            self.sign = '+'
        else:
            self.sign = '-'

    @staticmethod
    def sqrt(number):
        number = Number.to_number(number)
        l = 1
        r, a = number / 2
        r += 1
        rez = Number('0')
        while l <= r:
            m, a = (r + l) / 2
            if m * m <= number:
                rez = m
                l = m + 1
            else:
                r = m - 1
        return rez

    @staticmethod
    def to_number(value):
        if isinstance(value, str):
            return Number(value=value)
        if isinstance(value, int):
            return Number(value=str(value))
        if not isinstance(value, Number):
            raise TypeError
        else:
            return value

    @staticmethod
    def to_string(digits: list):
        """
        method for converting digits to str
        :param digits: digits in number
        :return: str
        """
        s = ''
        for digit in digits:
            s += str(digit)
        return s

    @staticmethod
    def remove_leading_zeros(number):
        k = 0
        for c in number.digit:
            if c == 0:
                k += 1
            else:
                number.digit = number.digit[k:]
                number.s = number.s[k:]
                return
        if k == len(number):
            number.digit = number.digit[:1]
            number.s = str(number.digit[0])
            a = 1

    @staticmethod
    def solve(m: list, b: list):
        m_, b_ = [], []
        for i in range(len(m)):
            m_.append(Number.to_number(m[i]))
            b_.append(Number.to_number(b[i]))
        m, b = m_, b_
        M = Number('1')
        for x in m:
            M *= x
        m_list = []
        for x in m:
            n, m_ = M / x
            m_list.append(n)
        n = []
        for i in range(len(m)):
            a = m_list[i]
            b_ = Number('1')
            m_ = m[i]
            c, k = a / m_
            a -= c * m_
            x = b_ * a ** (Number.phi(int(str(m_))) - 1)
            c, k = x / m_
            n.append(k)
        s = Number('0')
        for i in range(len(m)):
            ss = b[i] * n[i] * m_list[i]
            s += ss
        n, m_ = s / M
        return m_

    @staticmethod
    def phi(n):
        amount = 0
        for k in range(1, n + 1):
            if math.gcd(n, k) == 1:
                amount += 1
        return amount

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __mod__(self, other):
        other = Number.to_number(other)
        n, m = self / other
        return m

    def __abs__(self):
        n = Number(self.value)
        n.sign = '+'
        return n

    def __len__(self):
        return self.digit.__len__()

    def __getitem__(self, item):
        return self.digit[item]

    def __repr__(self):
        return self.value
