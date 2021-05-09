import math
from base64 import b64encode
from ctypes import *
import ctypes.util
import os
import platform

#DLL_NAME: str

#if platform.system() == 'Darwin':
#    DLL_NAME = 'libfast.dylib'
#elif platform.system() == 'Linux':
#    DLL_NAME = 'libfast.so'
#elif platform.system() == 'Windows':
#    DLL_NAME = 'libfast.dll'
#else:
#    raise SystemError("Unsupported platform", platform.system())

#os.add_dll_directory("D:\Code\python\Lab1Cript\Lab2")
#DLL_FULLNAME = ctypes.util.find_library('libfast')
#DLL_FULLNAME = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + DLL_NAME
#fast_lib = ctypes.cdll.LoadLibrary(DLL_FULLNAME)
#fast_lib = ctypes.cdll.LoadLibrary("D:\\Code\\python\\Lab1Cript\\Lab2\\build\\fast\\" + DLL_NAME)
#fast_lib.str_wrapper.restype = c_char_p
#fast_lib.str_wrapper.argtypes = [c_char_p, c_char_p,]

#fast_lib.mul.restype = c_ulonglong
#fast_lib.mul.argtypes = [POINTER(c_ulong), POINTER(c_ulong), ]

#fast_lib.powint.restype = c_ulonglong
#fast_lib.powint.argtypes = [POINTER(c_int), POINTER(c_int), ]

class Number:
    def __init__(self, value: str):
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

    def __floordiv__(self, other):
        other = Number.to_number(other) 
        a, b = self.__truediv__(other)
        return a

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

    def __and__(self, other):
        #other = Number.to_number(other)
        if isinstance(other, int):
            return int(self) & other
        elif isinstance(other, Number):
            return int(self) & other
        else:
            raise TypeError

    def __rshift__(self, other):
        #other = Number.to_number()
        if isinstance(other, int):
            return int(self) >> other
        elif isinstance(other, Number):
            return int(self) >> other
        else:
            raise TypeError

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
        #if int(self).bit_length() <= 10 and int(other).bit_length() <= 10:
        #    int_self = c_ulong(int(self))
        #    int_other = c_ulong(int(other))
        #    print("mul res: ", fast_lib.mul(byref(int_self), byref(int_other)))
        #    n = Number.to_number(fast_lib.mul(int_self, int_other))
        #else:
        #self_str: str = Number.to_string(self)
        #other_str: str =  Number.to_string(other)

        #self_bytes = self_str.encode('utf-8')
        #other_bytes = other_str.encode('utf-8')
        #self_bytes: bytes = self_str.encode('utf-8')
        #other_bytes: bytes = other_str.encode('utf-8')
        #mul_res = fast_lib.str_wrapper(self_bytes, other_bytes)
        #mul_res = mul_res.decode('utf-8')
        #n = Number.to_number(mul_res)
        n = Number.to_number(self.karatsuba_rec(int(self), int(other)))
        if self.sign == '-' and other.sign == '+':
            n.change_sign()
        elif self.sign == '+' and other.sign == '-':
            n.change_sign()
        else:
            return n
        return n


    def karatsuba_rec(self, x, y):
        """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
        if x < 10 and y < 10:
            return x * y

        num1_len = len(str(x))
        num2_len = len(str(y))

        n = max(num1_len,num2_len)

        
        nby2 = round(n/2)

        num1 = x // (10 ** nby2)
        rem1 = x % (10 ** nby2)

        num2 = y // (10 ** nby2)
        rem2 = y % (10 ** nby2)

        ac = self.karatsuba_rec(num1, num2)
        bd = self.karatsuba_rec(rem1, rem2)
        ad_plus_bc = self.karatsuba_rec(num1 + rem1, num2 + rem2) - ac - bd

        return (10 ** (2*nby2))*ac + (10 ** nby2)*ad_plus_bc + bd

    def _div(self, other):
        other = Number.to_number(other)
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
        #return Number.to_number(pow(int(self), int(b)))
        #if int(self).bit_length() <= 14 or int(b).bit_length() <= 14:
        #    int_self = c_int(int(self))
        #    int_other = c_int(int(b))
        #    result = fast_lib.powint(byref(int_self), byref(int_other))
        #    result = int(result) 
        #    return Number.to_number(result) 
        if b == 0:
            return 1
        elif b % 2 == 1:
            return self * self._pow(b - 1)
        else:
            n, m = b / 2
            a = self._pow(n)
            return a * a
        

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
        if mode is None:
            return first.__pow__(second)
        mode = Number.to_number(mode)
        p = first.__pow__(second)
        return p.__mod__(mode)

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
        """
        method for converting object to Number
        :value: number like object
        :return: Number
        """
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

    def as_binary(self):
        num = int(self)
        return bin(num)
    
    def as_hex(self):
        num = int(self)
        return hex(num)

    def as_bytes(self):
        #return bytes([int(self)])
        return self.value.encode('ascii')
    
    def as_base64(self):
        return b64encode(self.as_bytes())

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
    def solve(b: list, p: list, k: str):
        k:int = int(k)
        b = [int(x) for x in b]
        p = [int(x) for x in p]
        
        def _inv(a, m):
            m0 = m 
            x0 = 0
            x1 = 1
        
            if (m == 1) : 
                return 0
        
            while (a > 1) : 
    
                q = a // m 
        
                t = m 
        
                m = a % m 
                a = t 
        
                t = x0 
        
                x0 = x1 - q * x0 
        
                x1 = t 
        
            if (x1 < 0) : 
                x1 = x1 + m0 
        
            return x1

        prod = 1
        for i in range(0, k): 
            prod = prod * p[i] 
    
        result = 0

        for i in range(0,k): 
            pp = prod // p[i] 
            result = result + b[i] * _inv(pp, p[i]) * pp 
      
      
        return result % prod 

    @staticmethod
    def solve_eq(b, p, k):
        return 

    @staticmethod
    def phi(n):
        amount = 0
        for k in range(1, n + 1):
            if math.gcd(n, k) == 1:
                amount += 1
        return amount

    def __int__(self): 
        return int(self.value)

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
