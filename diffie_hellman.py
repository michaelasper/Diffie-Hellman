from math import sqrt, ceil, gcd
from sympy.ntheory import is_primitive_root, generate
from secrets import randbits

class Diffie(object):
    
    def __init__(self, key_size, secret, key=0):
        self.key_size = key_size
        self.sys_seed = randbits(key_size)
        if key==0:
            self.generate_public_secret()
        else:
            self.prime = key[0]
            self.g = key[1]
        self.secret = secret

    def get_common(self):
        return (self.prime, self.g)

    def generate_prime(self):
        self.prime = generate.nextprime(self.sys_seed)

    def generate_public_secret(self):
        self.generate_prime()
        self.find_prime_root_mod()
        return self.prime, self.g

    def find_prime_root_mod(self):
        for x in range(2,self.prime):
            if is_primitive_root(x,self.prime):
                self.g = x
                break
    
    def compute_shared(self):
        return pow(self.g, self.secret, self.prime)

    def get_shared_secret(self, shared):
        return pow(shared, self.secret, self.prime)
        