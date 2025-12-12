#Nhap so nguyen duong a co 3 chu so. Tinh tong cac chu so cua a
"""a = int(input(" nhap so nguyen duong co 3 chu so "))
print(" Tong cac chu so cua a ", a//100 + (a//10)%10 + a%10)"""
#Nhap ba so nguyen a, b, c. Dua ra tong min(a,b,c) + max(a,b,c)
"""a = int(input(" nhap so nguyen a: "))
b = int(input(" nhap so nguyen b: "))
c = int(input(" nhap so nguyen c: "))
print("tong gia tri nho nhat va gia tri lon nhat cua a,b,c la ", min(a,b,c) + max(a,b,c))"""
#Cho duong tron co ban kinh R. Tinh chu vi cua duong tron do, lam tron den 2 chu so thap phan
"""from math import pi
r = float(input(" nhap ban kinh R: "))
C = 2*r*pi
print(" Chu vi cua duong tron ban kinh ",r, "la :", round(C,1))"""
#Nhap 3 so nguyen duong a,b,c. Hay tim uoc chung lon nhat cua 3 so a,b,c
#Hint: su dung ham gcd() trong mo dun math
#c1
"""a = int(input(" nhap so nguyen duong a: "))
b = int(input(" nhap so nguyen duong b: "))
c = int(input(" nhap so nguyen duong c: "))
d = min(a,b,c)
e=0
for i in range(1,d+1):
    if a%i==0 and b%i==0 and c%i==0:
        e=i
print(" Uoc chung lon nhat cua ",a , b, c, "la: ",e)"""
#C2
"""from math import gcd
a = int(input(" nhap so nguyen duong a: "))
b = int(input(" nhap so nguyen duong b: "))
c = int(input(" nhap so nguyen duong c: "))
print(" Uoc chung lon nhat cua ",a , b, c, "la: ",gcd(a,b,c))"""
#Nhap 2 so nguyen duong a,b. Tim boi chung nho nhat cua a,b
#Hint: boi chung nho nhat = a*b chia phan chung
#C1
"""a=int(input(" nhap so nguyen duong a: "))
b=int(input(" nhap so nguyen duong b: "))
for i in range( max(a,b), a*b +1):
    if i%a==0 and i%b==0:
        print(" Boi chung nho nhat cua ",a,"va",b, "la" ,i)
        """
#C2
"""from math import gcd
a = int(input(" nhap so nguyen duong a: "))
b = int(input(" nhap so nguyen duong b: "))
print(" Boi chung nho nhat cua ",a, " va ",b, "la", a*b//gcd(a,b))"""



    

