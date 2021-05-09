import time
from apa import LongA
from math import gcd, ceil, sqrt, floor
from random import randint, randrange


class RSA:
    def __init__(self, num_bits):
        self.input_message = str()
        self.num_bits = num_bits
        self.prime1 = 0
        self.prime2 = 0
        self.modul = 0
        self.public_keys = tuple()
        self.private_keys = tuple()

    def __genprime(self, k):
        x = ""
        k = int(k)
        for y in range(k):
            x = x + "1"
        y = "1"
        for z in range(k-1):
            y = y + "0"
        x = int(x,2)
        y = int(y,2)
        p = 0
        while True:
            p = randrange(y,x)
            if self.__rabin_miller(p):
                break
        return p

    def gen_private_keys(self):
        gdc, x, d = self.__gcdExtended(self.public_keys[0], self.public_keys[1])
        self.private_keys = (self.public_keys[0], d)

    def get_public_keys(self):
        e = 65537
        while True:
            self.prime1 = self.__genprime(self.num_bits//2)
            if self.prime1 % e != 1:
                break
        
        while True:
            self.prime2 = self.__genprime(self.num_bits//2)
            if self.prime2 % e != 1:
                break

        N = self.prime1*self.prime2
    
        lam = self.__carmichael(int(N))

        if gcd(e, lam) == 1:
            self.public_keys = (N, e)
        else:   
            e_test = 0
            while True:
                e_test = randint(2, lam)
                if e_test % 2 == 0:
                    continue
                else:
                    if self.__rabin_miller(e_test):
                        if gcd(e_test, lam) == 1:
                            break   
        
            e = e_test
        self.public_keys = (N, e)

    def __gcdExtended(self, a, b): 
        if a == 0 :  
            return b,0,1
                
        gcd, x1, y1 = self.__gcdExtended(b%a, a) 
    
        x = y1 - (b//a) * x1 
        y = x1 
        
        return gcd, x, y

    def __rabin_miller(self, p):
        if(p < 2):
            return False
        if p != 2 and p % 2 == 0:
            return False
        s = p - 1
        t = 0
        while(s % 2 == 0):
            s >>= 1
            t += 1

        for i in range(20):
            a = randint(2, p - 2)
            #a_temp = int(a)
            #s_temp = int(s)
            #p_temp = int(p)
            #b = LongA.to_number(pow(a_temp, s_temp, p_temp))
            b = pow(a, s, p)
            if b == 1 or b == p - 1:
                continue
            for i in range(t):
                b = (b * b) % p

                if b == 1:
                    return False
                if b == p - 1:
                    break

        return True

    def __carmichael(self, n: int):
        n=int(n)
        k=2
        a=1
        alist=[]

        while not ((gcd(a,n))==1):
            a=a+1

        while ((gcd(a,n))==1) & (a<=n) :
            alist.append(a)
            a=a+1
            while not ((gcd(a,n))==1):
                a=a+1

        timer=len(alist)
        while timer>=0:
            for a in alist:
                if (a**k)%n==1:
                    timer=timer-1
                    if timer <0:
                        break
                    pass
                else:
                    timer=len(alist)
                    k=k+1
        return k

    def encode(self, message: str):
        words = message.split()
        encrypted = []
        for word in words:
            encrypted_word = []
            for c in word:
                c_ascii = ord(c)
                c_cypher = pow(c_ascii, self.public_keys[0], self.public_keys[1])
                encrypted_word.append(c_cypher)
            encrypted.append(encrypted_word)

        return encrypted


    def decode(self, message):
        decoded_message = ""
        for word in message:
            decoded_word = ""
            for cypher in word:
                m = pow(cypher, self.private_keys[1], self.private_keys[0])
                m = chr(m)
                decoded_word = decoded_word + m
            decoded_message = decoded_message + decoded_word
        return decoded_message

class Bob:
    def __init__(self, message, public_keys = None):
        self.message = message
        self.public_keys = public_keys
        self.RSA = RSA(10)
        self.RSA.input_message = self.message
    
    def code_messages(self):
        self.RSA.public_keys = self.public_keys
        self.message = self.RSA.encode(self.message)
    
class Alice:
    def __init__(self):
        self.message = None
        self.public_keys = list()
        self.private_keys = list()
        self.RSA = RSA(10)

    def create_keys(self):
        self.RSA.get_public_keys()
        self.public_keys = self.RSA.public_keys
    
    def decode_message(self):
        self.RSA.input_message = self.message
        self.RSA.gen_private_keys()
        self.private_keys = self.RSA.private_keys
        print(f"Pricate keys: {self.private_keys}")
        self.message = self.RSA.decode(self.message)
        
"""
def rabin_miller(p):
    if(p < 2):
        return False
    if p != 2 and p % 2 == 0:
        return False
    s = p - 1
    t = 0
    while(s % 2 == 0):
        s >>= 1
        t += 1

    for i in range(20):
        a = randint(2, p - 2)
        a_temp = int(a)
        s_temp = int(s)
        p_temp = int(p)
        b = LongA.to_number(pow(a_temp, s_temp, p_temp))
        #b = LongA.pow(a, s, p)
        if b == 1 or b == p - 1:
            continue
        for i in range(t):
            b = (b * b) % p

            if b == 1:
                return False
            if b == p - 1:
                break

    return True
"""
def miller_rabin(n):

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(10):
        a = randrange(2, n - 1)
        a_temp = int(a)
        s_temp = int(s)
        p_temp = int(n)
        x = LongA.to_number(pow(a_temp, s_temp, p_temp))
        #x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            a_temp = int(x)
            s_temp = int(s)
            p_temp = int(n)
            x = LongA.to_number(pow(a_temp, 2, p_temp))
            #x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def genprimeBits(k):
    x = ""
    k = int(k)
    for y in range(k):
        x = x + "1"
    y = "1"
    for z in range(k-1):
        y = y + "0"
    x = int(x,2)
    y = int(y,2)
    p = 0
    while True:
        p = randrange(y,x)
        p = LongA(str(p))
        if miller_rabin(p):
            break
    return p
            

#inp = input("Long number: ")
#inp = LongA(inp)
#print(f"is prime: {rabin_miller(inp)}")
#print(f"is prime: {miller_rabin(inp)}")
#inp = input("Number of bits: ")
#inp = LongA(inp)
#ans = genprimeBits(inp)
#print(f"rand prime number with {inp} bits: {ans}")
#print(f"ans as binary {ans.as_binary()}")
#print(f"ans as base64 {ans.as_base64()}")
#print(f"ans as bytes object {ans.as_bytes()}")

MESSAGE:str = "HELLO"
Bob = Bob(MESSAGE)
Alice = Alice()
Alice.create_keys()
print(f"Public keys {Alice.public_keys}")
Bob.public_keys = Alice.public_keys
Bob.code_messages()
print(f"{MESSAGE} is now Encoded message {Bob.message}")
Alice.message = Bob.message
Alice.decode_message()
print(f"massage decoded by Alice: {Alice.message}")
