#De quy quay lui
    # Mỗi thành phần x[i] có thể nhận giá trị từ một tập hợp D[i]
"""
def Try(i):     #Ham x[i] tu D[i]
    for a in D[i]:  #Tim kiem lua chon
        if < x[i] nhan duoc gia tri a ?>:   #Kiem tra rang buoc khi gan a cho x[i]
            x[i] = a    #buoc thu de xay dung loi giai
            if (i == n-1):  #dieu kien dung lai la gia tri cuoi cung x[n-1]
                <Hoan thanh bo nghiem>
            else:
                Try(i+1)    #Goi de quy de tiep tuc xay dung x[i + 1]
#Bat dau xay dung thanh phan dau tien
Try(0)
"""
#De quy co nho
#La mot dang quy hoach dong cua de quy
#Neu lam theo de quy binh thuong:
"""
def Fibo(i):
    if n <=2:
        return 1
    else:
        return Fibo(n-1) +  Fibo(n-2)
"""
#Neu lam theo de quy co nho:
"""
n = 100
F = [0 for i in range(1,n+1)]     #F0, F1,...Fn
def Fibo(n):
    if n <= 2:
        F[n] = 1
        return 1
    #Neu F[n-1] chua duoc tinh thi goi de quy Fibo[n-1] de tinh
    if F[n-1] == 0:
        F[n-1] = Fibo(n-1)
    #Neu F[n-2] chua duoc tinh thi goi de quy Fibo(n-2) de tinh
    if F[n-2] == 0:
        F[n-2] = Fibo(n-2)
    return F[n-1] + F[n-2]
x = Fibo(n)
print(x)
"""
"""
#BT: Nhi phan den 3 so:
n = 3
x = [0 for i in range(n)]
def nhiphan(a):
    for i in range(2):
        x[a] = i
        if a == n -1:
            print(x)
        else:
            nhiphan(a+1)
print(nhiphan(0))
"""
#BT1: Tinh tong cac so hang trong mot danh sach bang de quy
"""
F = [....]  #tu 0 -> n-1
S[i] = S[i-1] + F[i]
"""
"""
n = int(input("Nhap so phan tu cua danh sach: "))
F = [int(input()) for i in range(n)]#   danh sach luu bien
#S = [0 for i in range(n)]   #danh sach tong den vi tri i
n = n-1
def tinh_tong(n):   #tinh tong den chi so n
    if  n == 0:
        return F[0]
    else:
        return tinh_tong(n-1) + F[n]
print(tinh_tong(n))
"""
#BT2. Uoc chung lon nhat cua hai so nguyen duong
"""
a,b
a > b
d = UCLN (a,b) = UCLN(b,r) if r ==0 => UCLN b
"""
"""
def ucln(a,b):
    r = a % b
    if r == 0:
        return b
    else:
        return ucln(b,r)
print("Nhap vao hai so can tim UCLN: ")
a = int(input())
b = int(input())
h, k= max(a,b), min(a,b)
print("UCLN la: ",ucln(h,k))
"""
#BT3. Tinh luy thua a^n bang de quy
"""
def luythua(a,n):
    if n == 0:
        return 1
    else:
        return luythua(a,n-1) * a

a = int(input("Nhap co so: "))
b = int(input("Nhap so mu: "))
print(f"Luy thua {a} mu {b} la: ",luythua(a,b))
"""
#BT4. Bai toan liet ke hoan vi:
"""
n = int(input("Nhap so n: "))
x = [0 for i in range(n)]
def hoanvi(a):
    for i in range(1, n + 1):
        if i not in x:
            x[a] = i
            if a == n-1:
                print(x)
            else:
                hoanvi(a+1) #goi cau nay de tiep tuc xay dung tie
            x[a] = 0 # cau lenh hoan tac vi khi xet thi cac vi tri o phia sau
                    # chua co gia tri
print(hoanvi(0))
"""
#BT5.Bai toan thap ha noi
def Chuyen_dia(n, A, C, B): #Diem den A-> B: trung gian C
    if n == 1:
        print("Chuyen dia: ",n, "tu ",A, "--> " ,B)
    else:
        Chuyen_dia(n-1, A, B, C)    #Doi diem den A - > C: trung gian B
        print("Chuyen dia: ",n, "tu" ,A, "--> ",B)
        Chuyen_dia(n-1,C, A, B)     #Diem den C-> B: trung gian A
n = int(input("Nhap so dia can chuyen: "))
Chuyen_dia(n, "A", "C", "B")
        







