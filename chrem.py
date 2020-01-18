"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

from euklidian import gcd, extended_gcd

class CongruenceModulo:
    def __init__(self, x, modulo):
        self.x = x
        self.modulo = modulo

    def normalize(self):
        self.x = self.x % self.modulo # Works also for negative numbers

def chrem(congruence1, congruence2):
    n1 = congruence1.modulo
    n2 = congruence2.modulo
    # x = n2 * a1 * u + n1 * a2 * v
    #     mod n1        mod n2
    nsgcd = gcd(n1, n2)

    n1 = n1 // nsgcd
    n2 = n2 // nsgcd

    erw_result = extended_gcd(n2, n1)

    # print(erw_result.u, erw_result.v)

    solution = n2 * congruence1.x * erw_result.u + n1 * congruence2.x * erw_result.v

    return CongruenceModulo(solution, n1 * n2 * nsgcd)

def chrem_multiple(congruences):
    if len(congruences) == 0:
        return None
    if len(congruences) == 1:
        return congruences[0]
    # 2 or more congruences
    solution = chrem(congruences[0], congruences[1])
    for congruence in congruences[2::]:
        solution = chrem(solution, congruence)
    return solution

if __name__ == "__main__":
    # Input / Output

    equations = max(2, min(20, int(input("Enter number of congruences: "))))

    congruences = []

    for i in range(equations):
        print("")
        print("> Congruence " + str(i + 1) + ":")
        x = int(input("Enter x: "))
        modulo = int(input("Enter modulo: "))
        congruences.append(CongruenceModulo(x, modulo))

    solution = chrem_multiple(congruences)
    solution.normalize()

    print("")
    print("> Solution: " + str(solution.x) + " + " + str(solution.modulo) + "Z")