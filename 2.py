import  os
os.system("cls")

# n = 10
# for i in range(1, n + 1, 1):
#     print(i)

# n = int (input())
# for i in range (1, n + 1, 1):
#     if i % 2 == 0:
#         print(i)

#11 
# n = int(input())
# for i in range(1, n + 1, 1):
#     if i % 7 == 0 and i % 5 == 0 and i % 3 == 0:
#         print(i, end="  ")

#12
# n = int (input())
# yig = 0
# for i in range (1, n + 1):
#     if i % 3 == 0 and i % 8 == 0 and i % 2 == 0:
#        yig += i
# print(yig) 

#13
# yig = 0
# for i in range (40 , 180 + 1):
#     if i % 2 == 0 and i % 7 == 0 and i % 6 == 0 and i % 4 == 0:
#         yig  += i
# print(yig)

#14
# num = 0
# n = int (input())
# while n:
#     n //= 10
#     num += 1
# print(f"{num} ta xona")

#15
# a, b = map(int , input().split())
# yig = 0
# for i in range(a, b + 1 ):
#     yig += i
# print(yig)

#16
# son = int(input())
# for i in range(1, 10 + 1):
#     print(son,  " x ", i, " = ", son * i)

# A, B  = map(int, input().split())
# daraxt  = (B - A) + 1
# print(daraxt)

# n = int (input())
# son = 5; s = 0
# for i in range(1 ,  n):
#     x = son // 2
#     s = s + x
#     son = x * 3
# print(son)

# s = "salom"
# for i  in s:
#     print(i)
    
# soz = "salom bolalar "
# for i in range(len(soz)):
#     print(soz[i])

# soz = "salom bolalar "
# for i in range(len(soz)):
#     if soz[i] == ' ':
#         break
#     print(soz[i])

# soz = input("matn:   ")

# for i in soz:
#     if (i.isdigit()):
#         i = 'A'
#     print(i, end="")

# soz = input("gap kiriting:    ")
# text = ""
# for i in range(len(soz)):
#     if(soz[i].islower()):
#         text += soz[i].upper()
#     elif(soz[i].isupper()):
#         text += soz[i].lower
#     else:
#         text += soz[i]
# print(text)




# n = 5 
# for i in range(1,n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print("* ", end="")
#     print()


# n = 5
# for i in range(n):
#     print(' ' * (n - i - 1), end='')
#     print('* ' * (i + 1))




















