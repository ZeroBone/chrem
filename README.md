# chrem
Algorithm to solve a linear system of congruences using the Chinese remainder theorem. Works also for non-coprime divisors.
# Usage
Simply run `python chrem.py`
# Examples
* System of equations:
    ```
    x = 1 mod 27
    x = 25 mod 80
    ```
    Solution:
    ```
    Enter number of congruences: 2

    > Congruence 1:
    Enter x: 1
    Enter modulo: 27

    > Congruence 2:
    Enter x: 25
    Enter modulo: 80

    > Solution: 1945 + 2160Z
    ```
* System of equations (**not coprime divisors**):
    ```
    x = 1 mod 108
    x = 25 mod 80
    ```
    Solution:
    ```
    Enter number of congruences: 2

    > Congruence 1:
    Enter x: 1
    Enter modulo: 108

    > Congruence 2:
    Enter x: 25
    Enter modulo: 80

    > Solution: 1945 + 2160Z
    ```
* System of equations:
    ```
    x = 2 mod 3
    x = 2 mod 7
    x = 3 mod 10
    ```
    Solution:
    ```
    Enter number of congruences: 3

    > Congruence 1:
    Enter x: 2
    Enter modulo: 3

    > Congruence 2:
    Enter x: 2
    Enter modulo: 7

    > Congruence 3:
    Enter x: 3
    Enter modulo: 10

    > Solution: 23 + 210Z
    ```
* System of equations:
    ```
    x = 8 mod 35
    x = 3 mod 11
    x = 5 mod 6
    ```
    Solution:
    ```
    Enter number of congruences: 3

    > Congruence 1:
    Enter x: 8
    Enter modulo: 35

    > Congruence 2:
    Enter x: 3
    Enter modulo: 11

    > Congruence 3:
    Enter x: 5
    Enter modulo: 6

    > Solution: 113 + 2310Z
    ```
# License
Copyright (c) 2020 Alexander Mayorov.

This project is licenced under the MIT Licence.

Please leave a copyright notice if you use/modify this software or parts of it.

For more information see the LICENCE file.
