#Cach dung pakage
"""
import sys
sys.path.append("/Users/hien/Documents/PythonProjects")
from packagel.flowers import flowerlist
from packagel.sumlist import sum_list
#Tao mot doi tuong dung class flowerlist trong packagel
f1 = flowerlist()
f1.printflower()
#Su dung ham sum_list de tinh tong cac phan tu trong list
list = [1, 2, 3]
print("Tong cac phan tu: ",sum_list(list))
"""
#--------------
#BT1. Xay dung modunle co ten geometry.py gom cac lop:
"""
- Lop Circle() mo ta duong tron gom cac thuoc tinh va phuong thuc.
+ Thuoc tinh:
    Toa do tam ( x;y)
    Ban kinh r cua duong tron
+ Phuong thuc:
    getPerimeter(): tra ve chu vi duong tron
    getArea() tra ve dien tich hinh tron
    isIn(a,b) tra ve True neu (a,b) nam trong duong tron
    isOn(a,b) tra ve True neu (a,b) nam tren duong tron
    isOut(a,b) tra ve True neu (a,b) nam ngoai duong tron
- Lop Square() mo ta hinh vuong gom cac thuoc tinh va phuong thuc:
+ Thuoc tinh:
    canh a
+ Phuong thuc:
    getPerimeter()
    getArea
"""
"""
from geometry import Circle, Square
p1 = Circle(0, 0, 1)
print("Chu vi hinh tron la: ",p1.getPerimeter())
print("Dien tich hinh tron la: ",p1.getArea())
a = int(input("Nhap hoanh do: "))
b = int(input("Nhap tung do: "))
print(f"Toa do ({a}, {b} ) nam tren duong tron dung hay sai: ",p1.isOn(a,b))
"""
#BT2.
from number import gcd1, lcm, sumdivisor
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print(f"UCLN {a} va {b}: ", gcd1(a,b))
print(f"BCNN {a} va {b} ",lcm(a,b))
n = int(input("Nhap n: "))
print("Tong cac uoc: ",sumdivisor(n))




