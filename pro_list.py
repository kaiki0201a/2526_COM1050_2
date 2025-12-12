#Tao ma tran
#C1
"""
list1 = [[1,2,3] , [3,2,3] , [2,3,4]]
for i in range(3):
    for j in range(3):
        print(list1[i][j], end = " ")
    print() # de xuong dong tiep theo
"""
#C2.Tao ma tran m dong n cot
"""
m = int(input(" Nhap so dong: "))
n = int(input(" Nhap so cot: "))
A = [] #tao ma tran rong de chua kq cuoi cung
for i in range(m): #tao phan tu tung dong 1
    row = [] #khoi tao dong rong
    for i in range(n): #vi co n cot nen moi dong co n phan tu
        x = int(input())
        row.append(x) #them phan tu vao dong
    A.append(row) #them dong vao ma tran
print(" Ma tran vua nhap: ")
for x in A:
    print(x)
print("-----------")
print(" Neu khong dung for thi ket qua in ra la: ")
print(A)
"""
#C3
"""
m = int(input(" Nhap so dong: "))
n = int(input(" Nhap so cot: "))
#tao matran bang vong lap for
A =[[int(input()) for j in range(n)] for i in range(m)]
#vong for o ngoai se thuc hien truoc
print(" Ma tran vua nhap: ")
for x in A:
    print(x)
"""
#--------------------
#BT1.Xoay vong danh sach
#C1. Dung lenh pop() xoa phan tu cuoi
"""
a = []
n = int(input("Nhap vao so phan tu cua a: "))
for i in range(n):
    x=int(input())
    a.append(x)
b = []
b.append(a[n-1])
b.extend(a[:n-1])
print("Danh sach sau khi xoay vong: ",b)
"""
#BT2. Day cac phan tu lien tiep bang 0 dai nhat
#dung ham randint trong random de tao danh sach co gia tri phan tu la 0,1 bat ky
"""
from random import randint, uniform
a = []
n = int(input("Nhap vao so phan tu cua a: "))
for i in range(n):
    x = randint(0,1)
    a.append(x)
print(a)
i = 0
k = 0
h = 0
while i<n: 
    if a[i] == 0:
        k += 1
    if a[i] != 0 or i == n-1:
        if k >= h:
            h = k
            k = 0
    i +=1
print("Chuoi 0 dai nhat la: ",h)
"""
#BT3. Tong cac so hang lien tiep trong day co gia tri lon nhat
#Thuc hien chuyen khoi
"""
a = []
n = int(input("Nhap vao so phan tu cua a: "))
for i in range(n):
    x=int(input())
    a.append(x)
i = 1
b = h = 0
while i <= n:
    j = 0
    while j < n - i + 1:
        b = sum(a[j:j+i+1])
        if b >=h:
            h = b
            b = 0

        j +=1
    i +=1
print("Tong toi da: ",h)
"""
#BT4.Bai toan thong ke
#Dem so lan xuat hien bang PT: <ds>.count
#Xoa bo phan tu vua dem bang pt: del(<ds>)
"""
from random import randint, uniform
a = []
n = int(input("Nhap so phan tu cua a: "))
for i in range(n):
    x = int(input())
    a.append(x)
print(a)
a.sort()
while n>0 :
    b = a.count(a[0])
    print(" Phan tu ",a[0], "xuat hien ",b, "lan")
    del a[0:b] #xoa b phan tu co nghia la xoa tu chi so 0-> b-1
    n = n - b
"""
#BT5. Gop 2 danh sach
"""
from random import randint
n1 = int(input("Nhap so phan tu cua danh sach 1: "))
n2 = int(input(" Nhap so phan tu cua danh sach 2: "))
list1 = list2 = []
for i in range(n1):
    x = randint(0,10)
    list1.append(x)
for j in range(n2):
    y = randint(0,10)
    list2.append(y)
list1.sort()
list2.sort()
list3 = []
list3.extend(list1)
list3.extend(list2)
list3.sort()
print("List1 la: ",list1)
print("List2 la: ",list2)
print("List3 la: ",list3)
"""
#BT6.Day con tang dai nhat
"""
a = []
dp =[] #Khoi tao danh sach rong
n = int(input(" Nhap vao so phan tu cua danh sach: "))
for j in range(n):
    x = int(input())
    a.append(x)
    dp.append(1) #Xem tong lon nhat ban dau cua moi chi so la 1
k = 0
if a[1]>a[0]: #Xet thu cong vi tri dau
    dp[1] = 2
i = 2 #xac dinh tu vi tri i
hihi = [1,2,3] #tao mot danh sach de so sanh
while i < n:
    k = 0 #chay tu moi vi tri 0->j-1
    hihi.clear()
    hihi = [1] #them vao tung ham theo tung dp de so sanh
    while k < i:
        if a[i] > a[k]:
            hihi.append(dp[k] +1)
        k += 1
    dp[i] = max(hihi)
    i += 1
piw = max(dp)
print("Chuoi con co do dai lon nhat la",piw)
"""
#BT7. Tinh tong duong cheo chinh, phu cua ma tran
"""
from random import randint
m = int(input(" Nhap vao so dong cua ma tran: "))
n = int(input(" Nhap vao so cot cua ma tran: "))
A = []
for i in range(m):
    row = []
    for i in range(n):
        x = randint(1,10)
        row.append(x)
    A.append(row)
print("Ma tran vua nhap la: ")
for i in A:
    print(i)
print("-----------")
#00,11,22 voi m,n=3
#Voi duong cheo phu: [i][j] voi i chay tu n-1->0, j chay 0->n-1
s1 = s2 = 0
for i in range(n): #0, 1, 2, 3
    s1 = s1 + A[i][i] #00,11,22,33
    s2 = s2 + A[i][n-1-i] #03,12,21,30
print("Tong tren duong cheo chinh: ",s1)
print("Tong tren duong cheo phu: ",s2)
"""
#BT8. Ma tran chuyen vi
"""
from random import randint
m = int(input(" Nhap vao so dong cua ma tran: "))
n = int(input(" Nhap vao so cot cua ma tran: "))
A = []
for i in range(m):
    row = []
    for i in range(n):
        x = randint(1,10)
        row.append(x)
    A.append(row)
print("Ma tran vua nhap la: ")
for i in A: 
    print(i)
print("-----------")
B = []
#Ma tran Amxn -> Ma tran B nxm
for i in range(n): #n hang
    row2= []
    for j in range(m): #m cot
        row2.append(A[j][i]) # lay theo chieu doc
    B.append(row2)
print("Ma tran chuyen vi la: ")
for i in B:
    print(i)
"""
#BT9. Tich 2 ma tran
"""
from random import randint
m = int(input(" Nhap vao so dong cua ma tran A: "))
n = int(input(" Nhap vao so cot cua ma tran A, hang cua ma tran B: "))
p = int(input(" Nhap vao so cot cua ma tran B: "))
A = []
B = []
for i in range(m):
    row1 = []
    for i in range(n):
        x1 = randint(1,10)
        row1.append(x1)
    A.append(row1)
for i in range(n):
    row2 = []
    for i in range(p):
        x2 = randint(1,10)
        row2.append(x2)
    B.append(row2)
print("Ma tran A vua nhap la: ")
for i in A: 
    print(i)
print("-----------------")
print(" Ma tran B vua nhap la: ")
for i in B:
    print(i)
C = []
print("----test----")
for i in range(m):
    row3 = []
    for j in range(p):
        s = 0
        for k in range(n):
            x = A[i][k] * B[k][j]
            s = s + x
        row3.append(s)
    C.append(row3)
print("Tich cua ma tran A va B la: ")
for i in C:
    print(i)
"""




    

    
        


   




        













































