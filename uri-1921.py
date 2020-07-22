"""
Guilherme loves kites, kites of different colors, forms and sizes. He realized
that in order to kites become stable, and thus fly higher, they must have a taut
string connecting all pairs of non-neighboors tips. Despite being a very creative
and clever child, Guilherme doesn’t know how to determine the number of strings
necessary to make a kite of n sides stable. Could you help him?

Input:
The single line of the input contains an integer 3 ≤ n ≤ 105, the number of sides
of the kite.

Output:
Print a single number, the number of strings that Guilherme needs to make a kite
of n sides stable.
"""

n=float(input())
print(int(n*(n-3)/2))