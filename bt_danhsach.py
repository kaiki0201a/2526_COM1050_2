#1.Ham len(): tra ve so luong phan tu trong danh sach
        #Cach truy cap den cac phan tu: <dsach>[chiso]
        #Co the thay doi cac phan tu trong dsach: <ds>[chiso] = <newp>
#2.Cach lay phan tu lien tiep
    #<ds>[a:b] : lay tu a-> b-1
    #<ds>[:b] : lay tu 0 -> b-1
    #<ds>[b:] : lay tu b den het
    #<ds>[a:b:c] : lay a, a+c, a+2c...
#3.Phep noi va lap danh sach
    #Noi: <list1> + <list2>
    #Lap: <solanlap>*<list> hoac <list>*<solanlap>
#4.Cach them phan tu, mo rong danh sach
    #Them: <biendsach>.append(x) : them phan tu x vao cuoi danh sach
    #Mo rong: <ds1>.extend<ds2>
    #Phan biet: append them 1 phan tu, extend them n phan tu trong ds moi
#5. Phep toan in va not in
#6. PT <ds>.index(x) : tra ve chi so dau tien trong list = x
#7. Phep toan min, max trong danh sach
#8. Ham sum() : tinh tong cach phan tu trong danh sach

#-----------------------------------------------------------
#BT1. Tong so nguyen le.
"""
n = int(input(" Nhap so nguyen duong n: "))
a = []
for i in range(n):
    x = int(input(" Nhap gia tri: "))
    a.append(x)
s = 0
for j in a:
    if j %2 != 0:
        s += j
print(" Tong so nguyen le trong danh sach la: ",s)
"""
#BT2. Tong k so hand lien tiep co tong lon nhat
#Buoc 1: nhap vao danh danh gom n so nguyen
#Buoc 2: chia ra tung danh sach gom cac so lien tiep
#Buoc 3: tinh tong
"""
n = int(input(" Do dai cua danh sach la: "))
k = int(input(" So phan tu lien tiep can xet la: "))
a = []
for i in range(n):
    x = int(input(" Nhap vao gia tri cua danh sach: "))
    a.append(x)
print(a)
j = 0
s = 0
while j < n - k + 1:
    b = sum(a[j: j+k])
    if b > s:
        s =b
    j += 1
print(" Tong lon nhat voi " , k, " phan tu lien tiep la: ",s)
"""
#BT3. Sang so nguyen to Eratosthens
"""
from math import sqrt
N = 101
list1 = []
for i in range(N+1):
    list1.append(1) #xem ban dau tat ca deu la so nguyen so
list1[0] = list1[1] = 0 #Xet thu cong 2 so dau = 0
d = int(sqrt(N))
for i in range(2,d+1): #chi can xet toi phan nguyen cua can N la du
    if list1[i] == 1:
        for k in range(2, (N//i)+1): #loai bo phan boi di 
            list1[i*k] =0
print("Danh sach cac so nguyen to la: ")
for i in range(N):
    if list1[i] ==1:
        print(i , end = " ")
"""
#BT4. Khe ngan nuoc
"""
Mot binh chua nuoc gom n+1 vach ngan tao ra n khe nho.Cac vach duoc danh
        so tu 0->n (tu trai sang phai). Vach ngan thu i co do cao la Hi
        cac vach ngan cach nhau 1 don vi do dai.  Day moi vach ngan la mot hinh
        vuong do dai 1. Khi nuoc o vach ngan do cao h thi ta xem luong nuoc chua
        trong do la h(don vi khoi. Nguoi ra do day nuoc vao binh cho den khi max
        Tinh luong nuoc chua duoc trong binh
"""
#Huong di: xet luong nuoc co the chứa của từng khe
#Gặp khe lớn hơn thì bị chặn khe nhỏ hơn thì tràn qua
#Cần tìm 2 khe chặn từ 2 phía-> hai khe đó là 
#độ cao của khe sẽ  min của các khe năm 2 phía
"""
n1 = int(input(" Nhap so khe "))
n2 = n1 +1 #so vach ngan
a = []
for i in range(n2):
    x = int(input("Nhap chieu cao cua vach: "))
    a.append(x)
print(a)
s = 0
i = 1
while i < n1+1:
    L = max(a[:i])
    R = max(a[i:])
    s = s+ min(L,R)
    i +=1
print(" Tong luong nuoc la: ",s)
"""
#C2:
"""
n = int( input(" Nhap so khe nuoc n = "))
print(" Nhap n + 1 vach ngan ")
h = []
for i in range(n1+1):
    x = int(input())
    h.append(x)
s = 0
for i in range(1,n+1):
    L = max(h[:i])  #L bang max tu 0 -> i-1
    R = max(h[i:])  #R bang max tu i -> n
    s = s + min(L, R)
print(" Tong ",s)
"""
#BT5. Chon cac so
# Dung quy hoach dong trong lap trinh Dynamic programming
#Buoc khoi tao: L[0] = a0 , L[1] = max(a0,a1)
#Li: 2TH neu co chon ai-> khong chon a(i-1)-> max = ai + max(L(i-2),0)
         #neu khong chon ai => max = L(i-1)
#=> max (TH1,TH2)
n = int(input(" Do dai cua danh sach so can xet: "))
L = []
for i in range(n):
    x=int(input())
    L.append(x)
L[0] = L[0]
L[1] = max(L[0],L[1])
for i in range(2,n):
    L[i] = max(L[i-1], L[i] + max(L[i-2],0))
print("Tong max la: ", L[n-1])
    
    
















    
    




















