from itertools import permutations
a=input("Enter a string : ")
per = [''.join(p) for p in permutations(a)]
print(per)
