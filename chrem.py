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

    n1DividedTimes = 0
    while n1 % moduloGcd == 0:
        n1 = n1 // moduloGcd
        n1DividedTimes = n1DividedTimes + 1
    
    n2DividedTimes = 0
    while n2 % moduloGcd == 0:
        n2 = n2 // moduloGcd
        n2DividedTimes = n2DividedTimes + 1
    
    if (a1 - a2) % moduloGcd != 0:
        return None
    
    print(n1DividedTimes, n2DividedTimes)
    print("a = " + str(a1) + " b = " + str(a2))

    additionalCongruence = None

    if n1DividedTimes > n2DividedTimes:
        additionalCongruence = (a1, moduloGcd ** n1DividedTimes)
    else:
        additionalCongruence = (a2, moduloGcd ** n2DividedTimes)

    print((a1 % n1, n1), (a2 % n2, n2))
    mainSolution = chrem_coprime((a1 % n1, n1), (a2 % n2, n2))

    print(mainSolution, additionalCongruence)

    return chrem(mainSolution, additionalCongruence)




def chrem_old(congruence1, congruence2):
    (a1, n1) = congruence1
    (a2, n2) = congruence2

    moduloGcd = gcd(n1, n2)

    if moduloGcd == 1:
        return chrem_coprime(congruence1, congruence2)

    n1 = n1 // moduloGcd
    n2 = n2 // moduloGcd

    additionalCongruence = None
    
    if n1 % moduloGcd == 0:
        assert n2 % moduloGcd != 0
        # n2 % moduloGcd != 0 because otherwise the gcd would be incorrect
        # that means the second congruence must be added
        additionalCongruence = (a2 % moduloGcd, moduloGcd)
    elif n2 % moduloGcd == 0:
        assert n1 % moduloGcd != 0
        # n1 % moduloGcd != 0 because otherwise the gcd would be incorrect
        # add first congruence
        additionalCongruence = (a1 % moduloGcd, moduloGcd)
    else:
        # the new n1 and n2 cannot be further divided by the gcd
        # so we must add the missing terms
        if a1 % moduloGcd != a2 % moduloGcd:
            # the two additional and mandatory congruences are not equivalent
            # therefore, the congruence system cannot be solved
            return None
        # a1 = a2 mod gcd(n1, n2)
        additionalCongruence = (a1 % moduloGcd, moduloGcd)
    
    print("System:", [(a1 % n1, n1), (a2 % n2, n2), additionalCongruence])

    mainSolution = chrem_coprime((a1 % n1, n1), (a2 % n2, n2))

    print("Reduced to:", [mainSolution, additionalCongruence])

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
        print("> This congruence system is unsolvable.")
    else:
        print("> L = " + str(solution[0]) + " + " + str(solution[1]) + "Z")