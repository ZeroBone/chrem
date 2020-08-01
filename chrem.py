"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

from euklidian import gcd, extended_gcd

def chrem(congruence1, congruence2):
    (a1, n1) = congruence1
    (a2, n2) = congruence2

    (moduloGcd, u, v) = extended_gcd(n1, n2)

    if moduloGcd == 1:

        solution = n1 * a2 * u + n2 * a1 * v

        modulo = n1 * n2

        return (solution % modulo, modulo)

    if (a1 - a2) % moduloGcd != 0:
        # Unsolvable
        return None

    moduloLcm = (n1 // moduloGcd) * n2

    k = (a1 - a2) // moduloGcd

    solution = a1 - n1 * u * k

    return (solution % moduloLcm, moduloLcm)
    

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