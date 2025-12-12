#BT1: Tổng chữ số chung
"""
a = int(input(" Nhap vao so nguyen a: "))
b = int(input(" Nhap vao so nguyen b: "))
a1 = set(str(a))
b1 = set(str(b))
c = a1.intersection(b1)
s = 0
for x in c:
    s += int(x)
print(" Tong chu so chung cua a va b la: ",s)
"""
#BT2: Nhan phan thuong
"""
a: danh sach tat ca cac em hoc sinh
b: danh sach tat ca cac em hoc sinh nhan dot 1
c: danh sach tat ca cac em hoc sinh nhan dot 2
d: danh sach cac em nhan 2 quyen la b giao c ( intersection)
e: danh sach ca em nhan 1 lan: c hieu dx b ( symmetric_difference)
k: danh sach duoc nhan: d.union(e)
g: danh sach ca em khong nhan quyen nao: a - d - e ( difference)
"""
"""
n = int(input(" Tong so hoc sinh la: "))
n1 = int(input(" Tong so hoc sinh nhan qua dot 1: "))
n2 = int(input(" Tong so hoc sinh nhan qua dot 2: "))
print(" Danh sach hoc sinh: ")
a = set([str(input()) for i in range(n)])
print(" Danh sach hoc sinh nhan qua dot 1: ")
b = set([str(input()) for i in range(n1)])
print(" Danh sach hoc sinh nhan qua dot 2: ")
c = set([str(input()) for i in range(n2)])
d = c.intersection(b)
e = b.symmetric_difference(c)
k = d.union(e)
g = a.difference(k)
print("Ds cac em duoc nhan vo: ",k)
print("Ds cac em duoc nhan 1 quyen vo: ",e)
print("Ds cac em khong nhan duoc quyen nao: ",g)
"""
#BT3: Danh sach dai dien la danh sach gom ki tu dai dien theo chieu tang dan
n = int(input(" So phan tu danh sach a: "))
a = [int(input()) for i in range(n)]
b = set(a)
a = list(b)
print(a)




