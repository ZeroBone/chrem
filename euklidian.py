"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

def gcd(a, b):
    while True:
        if a == 0:
            return b
        b = b % a
        if b == 0:
            return a
        a = a % b

# Extended Euklidian Algorithm
class GCD_Result:
    def __init__(self, gcd, u, v):
        self.gcd = gcd
        self.u = u
        self.v = v

def extended_gcd(a, b):
    if a == 0:
        return GCD_Result(b, 0, 1)

    result = extended_gcd(b % a, a)

    u = result.u
    result.u = result.v - (b // a) * result.u
    result.v = u

    return result