import math
x=int(input("Intro x: "))
while x<=100: x=int(input("Intro x: "))
cd=int(math.log10(x))+1
pd=int(x//(10**(cd-1)))
ud=x%10
print(pd, ud)