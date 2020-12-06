"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

def gcd(a, b):
    while True:
        if b == 0:
            return a
        a = a % b
        if a == 0:
            return b
        b = b % a


def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)

    if b == 0:
        return (a, 1, 0)

    unPrev = 1
    vnPrev = 0
    unCur = 0
    vnCur = 1

    while True:
        qn = a // b
        newR = a % b
        a = b
        b = newR

        if b == 0:
            return (a, unCur, vnCur)

        # Update coefficients
        unNew = unPrev - qn * unCur
        vnNew = vnPrev - qn * vnCur

        # Shift coefficients
        unPrev = unCur
        vnPrev = vnCur
        unCur = unNew
        vnCur = vnNew