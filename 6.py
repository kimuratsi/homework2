import os
os.system("cls")

# j = lambda a, b: a + b
# print(j(2, 4))

# l = [2,5,8,9,6,3,1,4,5,3,58]

# print(l)
# print()
# sortson = sorted(l, key=lambda son : son)
# print(l)

# ls = [("Piyoz", 123456), ("Gosht", 159248), ("Guruch", 153022), ("Yog", 150000), ("Sabzi", 156324), ("Bodring", 123654)]
# ls1 = list(sorted(ls, key=lambda x: x[1], reverse=True ))
# print(ls1)

talaba = ['Diyora', 'Dilbek', 'Maftuna', 'Dildora', 'Madina']
ls = list(filter(lambda n: (n[0] == 'M'), talaba))
ls = list(filter(lambda n: (n[1] == 'a'), ls))
print(ls)
