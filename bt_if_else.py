#1.Giai pt bac 2:
"""from math import sqrt
a = float(input(" He so cua x^2 "))
b = float(input(" He so cua x "))
c = float(input(" He so cua tu do "))
print(" Phuong trinh bac 2 :", a ,"x^2 + ", b, "x +",c ," = 0")
d= b**2 - 4*a*c
if d<0:
    print(" PT vo nghiem ")
else:
    if d==0:
        print(" PT co nghiem kep x = ", -b/(2*a))
    else:
        print(" PT co 2 nghiem phan biet x1 =", (-b-sqrt(d))/(2*a) , ",x2 =", (-b+sqrt(d))/(2*a))
"""
#2. Phan loai tam giac(deu, vuong, thuong)
"""
a = float(input(" Nhap gia tri cua canh thu 1: "))
b = float(input(" Nhap gia tri cua canh thu 2: "))
c = float(input(" Nhap gia tri cua canh thu 3: "))
d = max(a,b,c)
h = min(a,b)
k = min(b,c)
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("day la 3 canh cua tam giac deu ")
    else:
        if h**2 + k**2 == d**2:
            print(" Day la 3 canh cua tam giac vuong")
        else:
            print(" Day la tam giac thuong ")
else:
    print("day khong phai la 3 canh cua 1 tam giac")
"""
#3. Giao doan
"""
a = int(input(" Nhap can duoi cua mien thu 1 "))
b = int(input(" Nhap can tren cua mien thu 1 "))
c = int(input(" Nhap can duoi cua mien thu 2 "))
d = int(input(" Nhap can tren cua mien thu 2 "))
h = max(a,c)
k = min(b,d)
if a<=b and c<=d:
    if h<=k:
        print( " Co ", k-h+1, " so nguyen thuoc giao doan cua 2 mien ")
    else:
        print( " Co 0 so nguyen thuoc giao doan cua 2 mien ")
else:
    print(" Ban da nhap sai can ")
"""
#Tim dien tich giao nhau cua 2 hinh chu nhat tren mat phang toa do Oxy
"""
Xa = int(input(" Nhap hoanh do cua can duoi ben trai cua hcn thu 1: "))
Ya = int(input(" Nhap tung do cua can duoi ben trai cua hcn thu 1: "))
Xb = int(input(" Nhap hoanh do cua can tren ben phai cua hcn thu 1: "))
Yb = int(input(" Nhap tung do cua can tren ben phai cua hcn thu 1: "))
Xc = int(input(" Nhap hoanh do cua can duoi ben trai cua hcn thu 2: "))
Yc = int(input(" Nhap tung do cua can duoi ben trai cua hcn thu 2: "))
Xd = int(input(" Nhap hoanh do cua can tren ben phai cua hcn thu 2: "))
Yd = int(input(" Nhap tung do cua can tren ben phai cua hcn thu 2: "))
Xh=Yh=Xm=Ym=Xk=Yk=Xn=Yn=0
if Yb>Yd:
    Xh=Xb
    Yh=Yb
    Xk=Xd
    Yk=Yd
    print(Yk)
    Xm=Xa
    Ym=Ya
    Xn=Xc
    Yn=Yc
else:
    Xk=Xb
    print(Yb)
    Yk=Yb
    Xh=Xd
    Yh=Yd
    print(Yk)
    Xn=Xa
    Yn=Ya
    Xm=Xc
    Ym=Yc
print(Ym,Yk)
if Ym> Yk:
    print(" Dien tich giao nhau = 0 ")
else:
    if Ym==Yk:
        if Xn>Xm:
            print(" Dien tich phan giao nhau la ", Xh-Xn)
        else:
            print(" Dien tich phan giao nhau la ", Xk-Xm)
    if Ym< Yk:
        p=Yk-Ym
        if Xn>Xm:
            print(" Dien tich phan giao nhau la ", (Xh-Xn)*p)
        else:
            print(" Dien tich phan giao nhau la ", (Xk-Xm)*p)
"""
#C2 phat trien tu bai 3
""" x thuoc hcn 1 <=> min(xa,xb)<x<max(xa,xb)
    y thuoc hcn 1 <=> min(ya,yb)< y < max(ya, yb)
    tuong tu => ...
    lai so sanh tiep -> he 4 pt giai tuong tu tren
    
        
    
