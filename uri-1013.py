import math
input1 = input().split(" ")
a,b,c = input1

maior = int((int(a)+int(b)+abs(int(a)-int(b)))/2)
result = int((int(maior)+int(c)+abs(int(maior)-int(c)))/2)
print(result,"eh o maior")