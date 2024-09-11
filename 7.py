import os 
os.system("cls")

# def hisobla(a : int , b: int):
#     try: 
#         natija = a  / b
#     except ZeroDivisionError:
#         print("NULLga bolib bolmaydi ")
#     except TypeError:
#         print("Bu string ")
#     else:
#         print(natija)

# hisobla(3 , 2)
"""

serya = "Muhammadrasul doskaga qarang.\nFarruhbek o`ynamang."

file = open("soz.txt", "w")
file.write(serya)
file.close()

f = open("soz.txt", "r")
matn = f.read()
print(matn, end="\n\n\n")


f.seek(0)
for i in f:
    for j in i:
        print(j, end="")
        
f.seek(0)
print("\n\n\n")
text = f.readline()
print(text)
f.seek(0)

print()
ls = f.readlines()
print(ls, end="\n\n")

for i in ls:
    for j in i:
        print(j, end="")
f.close()

file = open("soz.txt", "w")
lis = ["nand", "nvsbklf", "s;nfndf"]
file.writelines(lis)

for i in lis:
    file.write(i)
    file.write(" ")
f.close()
"""

file  = open("fact.txt")

matn = file.read()
ls, ls1 = [], [] 
for i in matn.split("\n"):
    ls.extend(i.split("."))
for j in ls:
    ls1.extend(j.split())
natija = sorted(ls1, key=len)
print(natija)
# print("max ==>   ", natija[-1])

ls, ls1 = [],[]

for i in natija:
    ls.append(i)
    ls1.append(len(i))

dic = dict(zip(ls, ls1))

print(dic)

file.close()










