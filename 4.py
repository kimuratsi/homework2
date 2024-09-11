import os
os.system("cls")

"""
l1 = [int(input()) for i in range(int(input("N1:     ")))]
l2 = [int(input()) for i in range(int(input("N2:     ")))]
l3 = [int(input()) for i in range(int(input("N3:     ")))]
l4 = [int(input()) for i in range(int(input("N4:     ")))]
l = [l1,l2,l3,l4]
print(l) ; katta = 0
for i in l:
    if sum(i) > katta:
        katta = sum(i)
for j in l:
    if sum(j) == katta:
        print(j)
"""

# n = int (input())
# ls = [n*[]]

# for i in range(n):
#     ls[i] = (input("N:  ").split())
# print(ls)


# ls = [int(input()) for i in range(int(input("N:  ")))]
# soz = input("string:  ")
# print(ls, soz)

# for i in range(len(ls)):
#     ls[i] = soz + str(ls[i])

# print(ls)
"""
ls = [int(input)]
print(ls)

for i in range(100):
    m = ls.count(i)
    if m != 0:
        print(i," dan ", m, "ta")
"""


dic = {}
n  = int (input("N:   "))
for i in range(1, n + 1):
    k = input("Key:  ")
    dic[k] = input("Value:  ")
    
print(dic) 

for i in dic:
    b = dic.values()
    if b == "salom":
        d = dic.keys()
        dic = dic.pop(d)
        
print(dic)





