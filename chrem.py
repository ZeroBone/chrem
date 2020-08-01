"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

from euklidian import gcd, extended_gcd

def chrem_coprime(congruence1, congruence2):
    (a1, n1) = congruence1
    (a2, n2) = congruence2

    moduloGcd = extended_gcd(n2, n1)

    assert moduloGcd.gcd == 1

    solution = n2 * a1 * moduloGcd.u + n1 * a2 * moduloGcd.v

    modulo = n1 * n2

    return (solution % modulo, modulo)

def chrem(congruence1, congruence2):
    (a1, n1) = congruence1
    (a2, n2) = congruence2

    moduloGcd = gcd(n1, n2)

    if moduloGcd == 1:
        return chrem_coprime(congruence1, congruence2)

    if (a1 - a2) % moduloGcd != 0:
        return None

    moduloFactorN1 = 1

    while n1 % moduloGcd == 0:
        n1 = n1 // moduloGcd
        moduloFactorN1 = moduloFactorN1 * moduloGcd
    
    moduloFactorN2 = 1

    while n2 % moduloGcd == 0:
        n2 = n2 // moduloGcd
        moduloFactorN2 = moduloFactorN2 * moduloGcd

    additionalCongruence = None

    if moduloFactorN1 > moduloFactorN2:
        assert moduloFactorN1 % moduloFactorN2 == 0
        additionalCongruence = (a1 % moduloFactorN1, moduloFactorN1)
    else:
        assert moduloFactorN2 % moduloFactorN1 == 0
        additionalCongruence = (a2 % moduloFactorN2, moduloFactorN2)

    mainSolution = chrem_coprime((a1 % n1, n1), (a2 % n2, n2))
    print("1) Solving:", (a1 % n1, n1), (a2 % n2, n2), "=>", mainSolution)

    print("2) Solving:", mainSolution, additionalCongruence)

    return chrem(mainSolution, additionalCongruence)

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
        x = int(input("x is congruent to: "))
        modulo = int(input("... modulo: "))
        congruences.append((x, modulo))

    solution = chrem_multiple(congruences)

    print("")
    if (solution == None):
        print("> L = {}")
    else:
        print("> L = " + str(solution[0]) + " + " + str(solution[1]) + "Z")