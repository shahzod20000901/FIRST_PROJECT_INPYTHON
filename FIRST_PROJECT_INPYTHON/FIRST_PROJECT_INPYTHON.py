
import math
from sqlite3 import Date


# a=2
# b='saom'
# a=b
# b=3
# print(type(a))
# print(type(b))
# ism="ali \"bek\""
# print(ism)
# print(4/3)
# print(4//3)

# # a=5
# # b=10
# # print(a*b)
# # print(a**2)
# # print(b%a)


# a=-2
# b=4.3
# c=4
# print(b%a)
# a=2 **3 **2 # 3 ni  kvadrati 9, 2 ni 9 chi darajasi 512.
# print(a)
# print("-----------------------------------------------------------------")
# ###############################################################################

# #"faqat butun qismini oladi: "

# print(math.floor(5.99))
# print(f'{"Qiymat"}, {math.floor(5.99)}')
# print(math.ceil(5.99))
# print(round(5.99))
# # round 0.5 gacha oladi. misol 2.4 bo‘lsa 2 boladi
# # ceil 1.1 da  0.1 bo‘lsa ham 2 oladi 
# print("-----------------------------------------------------------------")
# print(a, b, c, sep=" | ")

# print("-----------------------------------------------------------------")

# ism =str(input('ismingizni yozing: '))
# print(ism)

# #bool True False

# a='Salom' #True
# b=''      #False
# print("-----------------------------------------------------------------")
# x=5
# y=6
# javob= x<y and x>y
# jami = x<y or x>y
# print(javob)
# print(jami)
# # True False=False
# # True True=True
# print("-----------------------------------------------------------------")
# a=1
# b=2
# c=3
# d=4
# print(" and , or")
# javob= (a<b or c>d) and (d>a and b>d)
# print(javob)
# s=10


# # str methods
# a='salom'
# b='hayr'

# print(a+b)
# print(a+' '+b)
# c=3
# print(a+' '+b+' '+ str(c))
# print("-----------------------------------------------------------------")

# javob=f'{a} {b} {c+5}'
# print(javob)
# print("-----------------------------------------------------------------")

# ism='alionlarnikidligimizda'
# print(ism[0])#javob a
# print(ism[-1])#javob a
# print(ism[1:4])#javob n
# print(ism[1:10:2]) #step 
# print(ism[::-1]) #teskarisiga
# print(ism[:7:3]) #
# print("-----------------------------------------------------------------")

# aralash='abrakaabra'
# print(aralash.upper()) #katta harf
# print(aralash.lower()) #kichik harf
# print(aralash.capitalize()) #faqat brinchi harfni kata qilish
# print(aralash.title()) #har bir so‘zni bosh harfini katta qilib beradi
# print("-----------------------------------------------------------------")
# print(aralash.count('ra'))#sanab beradi ra necha marta kelganligini
# print(aralash.find('a'))# birinchi uchragan a ni indeksini qaytaradi
# print(aralash.find('j')) # birinchi uchragan j ni indeksini qaytaradi
# print(aralash.find('br', 3)) 
# print(aralash.replace('a', 'o', 3))

# print("-----------------------------------------------------------------")
# print(aralash.isalpha()) #tekstda hamma simvollar harflarmi? shuni tekshiradi true yoki false qaytaradi  
# print(aralash.isdigit()) # tekstda sonlar bor yoki yoqligini tekshiradi
# #print(aralash.index('j'))#

# print("-----------------------------------------------------------------")
# x='4321'
# print(x.rjust(5, '*'))
print("1 VAZIFA --------------------------------------------")


ism=str(input(("Ismingizni kiriting: ")))
yosh=int(input(("Yoshingizni kiriting: ")))
print("-----------------------------------------------------------------")
print(f'{"Salom! "}, {ism}, {"Siz "}, {yosh}, {" yoshdasiz!"}')

print("2 VAZIFA --------------------------------------------")
a=int(input("Birinchi butun sonni kiriting: "))
b=int(input("Ikkinchi butun sonni kiriting: "))
print(f'{"Sonlar yig‘indisi: "}, {a+b}')
print("3 VAZIFA --------------------------------------------")
satr=str(input("Ixtiyoriy satr kiriting: "))
print(f'{"Satr uzunligi: "}, {len(satr)}')
print("4 VAZIFA --------------------------------------------")
kvadrat=int(input("Butun son kiriting: "))
print(f'{"Sonning kvadrati: "}, {pow(kvadrat, 2)}')
print("5 VAZIFA --------------------------------------------")
ism=str(input("Ismizzi kiriting: "))
print(ism.capitalize())
print("6 VAZIFA --------------------------------------------")
satr=str(input("Satr kiriting: "))
print(reversed(satr))
print("7 VAZIFA --------------------------------------------")
bir=str(input("Birinchisini kiriting: "))
ikki=str(input("Ikkinchisini kiriting: "))
print(f'{bir+" "}, {ikki}')
print("8 VAZIFA --------------------------------------------")
bir=int(input("Birinchisini kiriting: "))
ikki=int(input("Ikkinchisini kiriting: "))
print(f'{"Bo‘lish natijasi: "}, {bir/ikki}')
print("9 VAZIFA --------------------------------------------")
bir=int(input("Birinchisini kiriting: "))
ikki=int(input("Ikkinchisini kiriting: "))
uch=int(input("Uchinchisini kiriting: "))
print(sum(bir, ikki, uch)/3)
print("10 VAZIFA --------------------------------------------")
bir=int(input("Tug‘ilgan yilizni kiriting: "))
print(f'{"Sizning yoshingiz: "}, {Date.year-bir}')

