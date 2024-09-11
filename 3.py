import os
os.system("cls")

"""
# lst1 = []
# print(type(lst1))
# print(type(lst2))
# lst1 = [12, 11, 15, 158, 18, 18, 15]
# print(*lst1)
# print(lst1[5])
# for i in lst1:
#     print(i, end="  ")
# print("\n")
# for i in range(len(lst1)):
#     print(lst1[i], end="  ")

# lst2 = ["salom", 12, True, False, 123.321, "farruxbek"]
# for i in range(len(lst2)):
#     if (type(lst2[i]) == str or type(lst2[i]) == bool):
#         print(lst2[i])
# ls = list()
# print(ls)
# ls.append(15)
# n = int (input("N:  "))
# for i in range(n):
#     k = input()
#     ls.append(k)
# print(ls)

# n = int (input("N:  "))
# ls = list()
# for i in range(n):
#     yig = 1
#     k = int(input())
#     for j in range(1,k + 1):
#         yig *= j
#     ls.append(yig)
# print(ls)

# #APPEND
# ls= []
# ls = ["salom", 123, True]
# print(ls)
# ls.append(123.321)
# print(ls)

# #INSERT
# ls.insert(0, "qalay")
# print(ls)

# #REMOVE
# ls.remove(123)
# print(ls)

# #pop
# ls.pop(2)
# print(ls)
# d = ls.pop(1)
# print(d)
# print(ls)
"""

ls = list(input("List malumotlarini toldiring:  ").split())

print("1.Malumot qoshish")
print("2.malumot ochirish")
print("3.sortlash")
print("4.malumotlarini korish")
print("5.exit")

a = int (input("N:  "))
if a == 1:
    print("1.oxirdan malumot qoshish")
    print("2.berilgan indexdan qoshish")
    print("3.oxiridan n ta malumot qoshish")
    b = int(input("N:  "))
    if b == 1:
        k = input("Bitta malumot kiriting:  ")
        ls.append(k)
        print(ls)
    elif b == 2:
        c = int (input("Index:  "))
        d = input("Kiritiladigan malumot:  ")
        ls.insert(c, d)
    elif b == 3:
        n = int(input("Malumotlar hajmi:   "))
        ls1 = []
        print("malumotlarni kiriting: ")
        for i in range(n):
            ls1[i] = input()
        ls.extend(ls1)
    
elif a == 2:
    print("1.remove")
    print("2.pop")
    print("3.pop (index)")
    print("4.clear")
    c = int (input("N:  "))
    if c == 1:
        print(ls)
        k = input("ochirib tashlanadigan malumot:   ")
        ls.remove(k)
    elif c == 2: 
        ls.pop()
        print(ls)
    elif c == 3:
        print(ls)
        l = int(input("index:  "))
        ls.pop(l)
        print(ls)
    elif c == 4:
        ls.clear()
        print(ls)
        
elif a == 3:
    print("1.togri tartibda")
    print("2.teskari sortlash")
    print("3.teskari aylantirish")
    m = int(input("N:  "))
    if m == 1:
        print(ls)
        ls.sort()
        print(ls)
    elif m == 2:
        print(ls)
        ls.sort(reverse=True)
        print(ls)
    elif m == 3:
        print(ls)
        ls.reverse
        print(ls)

elif a == 4:
    print(ls)
elif a == 5:
    print("dastur yakunlandi")















