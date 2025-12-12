#BT1. Tao mot tuple gom n so nguyen va tinh tong
#Cach tao tuple
# Cach 1: tao list roi chuyen qua tuple
# Cach 2: tao mot tuple = (). Lan luot nhap cac thanh phan, luu chung thanh bo gom 1 ptu

#C1
"""
n = int(input(" Nhap so phan tu cua tuple: "))
print("Nhap ", n, "phan tu: ")
list = [int(input()) for i in range(n)]
tuple1 = tuple(list1)
print("tuple nhap vao : ",tuple1)
sum_odd = sum_even = 0
for x in tuple1:
    if x%2 == 0: sum_even += x
    else: sum_odd += x
print(" TOng cac phan tu le: ",sum_odd)
print(" TOng cac phan tu chan: ",sum_even)
"""
"""
#C2
n = int(input(" Nhap so phan tu cua tuple: "))
print("Nhap ", n, "phan tu: ")
tuple1 = ()
for i in range(n):
    x = int(input())
    tuple1 += (x,)
print("tuple nhap vao: ",tuple1)
sum_odd = sum_even = 0
for x in tuple1:
    if x%2 == 0: sum_even += x
    else: sum_odd += x
print(" TOng cac phan tu le: ",sum_odd)
print(" TOng cac phan tu chan: ",sum_even)
"""
#BT2
# Nhan xet: dua ve 1 bo roi dung so sanh tuple no se so sanh tung muc khoi l-gtri
#C1. Chay
"""
n = int(input(" Nhap so do vat n = "))
list1 = [] # danh sach
print(" Nhap ",n, " khoi luong: ")
listA = [int(input()) for i in range(n)]
print("Nhap ",n, " gia tri: ")
listB = [int(input()) for i in range(n)]
# : tao duoc 2 list la list khoi luong va list gia tri
for i in range(n):
    x = (listA[i], listB[i]) #khai bao tuple, gom thanh 1 bo
    list1.append(x) #danh sach list1 la danh sach gom cac bo
list1.sort()    #dung so sanh 2 tuple
print(" Danh sach do vat da duoc sap xep: ")
for i in range(n):
    print(list1[i][0]," ",list1[i][1])
"""
#C2: dung zip
"""
n = int(input(" Nhap so do vat n = "))
list1 = [] # danh sach
print(" Nhap ",n, " khoi luong: ")
listA = [int(input()) for i in range(n)]
print("Nhap ",n, " gia tri: ")
listB = [int(input()) for i in range(n)]
list1 = list(zip(listA, listB))
print(list1)
list1.sort()
print("-----")
print(list1)
print(" Danh sach do vat da duoc sap xep: ")
for i in range(n):
    print(list1[i][0]," ",list1[i][1])
"""
#BT3:Sap xep thong tin
n = int(input(" Nhap so hoc sinh: "))
list1 = [] # danh sach
print(" Nhap diem mon toan: ")
listA = [int(input()) for i in range(n)] #mon tin la A
print("Nhap diem mon tin: ")   #mon toan la B
listB = [int(input()) for i in range(n)]
print("Nhap diem mon anh: ")
listC = [int(input()) for i in range(n)]
""" cach basic
for i in range(n):
    x = ( listA[i] , listB[i], listC[i])
    list1.append(x)
list1.sort()
"""
list1 = list(zip(listA, listB, listC))
list1.sort(key = lambda hs: hs[1])
print(" Danh sach hoc sinh da duoc sap xep: ")
for i in range(n):
    print(list1[i][0], list1[i][1], list1[i][2], sep = " ")






    






