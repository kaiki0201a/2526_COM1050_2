#Liet ke cac khoa
"""
dict1 = {1: 2, 3: "Toan", 2: "Tin" }
print(" Cac khoa cua tu diem la: ")
for x in dict1:
    print(x, end = ", ")
"""
#Liet ke cac gia tri
    #C1
"""
dict1 = {1: 2, 3: "Toan", 2: "Tin" }
print(" Cac gia tri cua tu dien la: ")
for x in dict1:
    print(dict1[x], end = ", ")
"""
    #C2:
    #Phuong thuc values()
"""
dict1 = {1: 2, 3: "Toan", 2: "Tin"}
print("Cac gia tri cua tu dien: ")
for x in dict1.values():
    print(x, end = ", ")
"""
#Liet ke ca khoa va gia tri
#Phuong thuc items()
"""
dict1 = {1: 2, 3: "Toan", 2: "Tin"}
print("Khoa va gia tri: ")
for x, y in dict1.items():  #dict.iteams se tao ra 1 tuple gom khoa va gia tri
    print(x,":", y)
"""
#Cac phep toan tren kieu tu dien
    #len : dem cap khoa: gia tri
    #Thêm một phần từ mới vào từ điển:< biến td>[newkey] = <value>
"""
dict1 = {1: 2, 3: "Toan", 2: "Tin"}
dict1[4] = "Ly"
print("Cac phan tu cua tu dien: ")
print(dict1)
"""
    #Thay doi gia tri
    #Xoá một phần từ thuộc từ điển
#Phuong thuc pop(): <biến td>.pop(khoá); xoá và trả về giá 
"""
dict1 = {1: 2, 3: "Toan", 2: "Tin"}
dict1.pop(3)
print("Cac phan tu cac tu dien: ")
print(dict1)
"""
    #Câch ngăn chặn lỗi trong pop: dict.pop( key, default_value)
#Phuong thuc popitem(): <bien td>.popitem(); xoá sau cùng hoặc được thêm vào sau cùng
#Phuong thuc del: del <bien td>[<khoá>]: xoá và không trả về giá 
#Phuong thuc clear: <bien td>.clear()
#Phep toan in: <key> in <biến từ điển>; trả về true nếu khoá có trong dict
#Phuong thuc get()
""" <biến từ điển>.get(k) : trả về giá trị của phần tử có khoá là k, nếu
trong dict không có khoá k thì trả về gtri None
     Dạng tham số: <biến td>.get(k, "giá  mặc định"):
     Trả về giá trị của phần từ có khoá là k. Trong trường hợp dict không chứa
     khoá k thì trả về giá trị mặc 
"""
"""
dict1 = {1: 2, 2: "Toan", 3: "Tin", 4: "Ly"}
print(dict1.get(2))
print(dict1.get(4))
print(dict1.get(5))
"""
# NOTE: Chi nhung kieu du lieu bat bien nhu str, int, float, tuple, bool moi
#       co the lam gia tri trong khoa cua dictionary
#----------BT--------
#BT1. Tao tu dien
"""
n = int(input("So phan tu cua tu dien: "))
list1 = [i for i in range(n)]
list2 = [str(input("Nhap ten: ")) for i in range(n)]
tudien = {}
for i in range(n):
    tudien[list1[i]] = list2[i]
print("Ket qua la: ")
for i, j in tudien.items():
    print(f" So: {i} co ten la: {j} ")
"""
#BT2: Thong ke diem thi
"""
n = int(input(" Nhap so hoc sinh: "))
i = 0
sodiem = {}
while i < n:
    ten = str(input("Ten hoc sinh la: "))
    diem = int(input(f" {ten} co so diem la: "))
    sodiem[ten] = diem
    i += 1
print(sodiem)
"""
#BT3: Tra cuu diem thi
"""
n = int(input(" Nhap so hoc sinh: "))
#Khoa se la so bao danh, ten va diem la gia tri, tao 2 list chua 2 thanh phan nay
print(" Nhap tat ca cac so bao danh: ")
list1 = [int(input()) for i in range(n)]
print(" Nhap ho - ten va diem thi tuong ung: ")
list2 = [(str(input("Ho ten: ")), int(input("Diem thi: "))) for i in range(n)]
i = 0
sotracuu = {}
while i < n:
    sotracuu[list1[i]] = list2[i]
    i +=1
"""
"""
for i , j in sotracuu.items():
    print(f" So bao danh: {i} ; Ho-ten: {j[0]}; Diem: {j[1]} ")
"""
"""
def tracuu(m):
    if m in sotracuu:
        return f" So bao danh: {m}; Ho-ten: {sotracuu[m][0]}; Diem: {sotracuu[m][1]} "
    else:
        return ("So bao danh khong ton tai!")
sbd = int(input("Nhap so bao danh can tra cuu: "))
print(sotracuu.get(sbd, "Khong ton tai sbd nay"))
"""
#BT4. Cap so hang co gia tri lien tiep
#xet 2 chi so i,j voi i<j; neu a[i] + 1 = a[j] thi tao thanh 1 cap so hang
"""
phan 1: chi so
phan 2: gia tri
"""
"""
n = int(input("Nhap so phan tu: "))
a = [int(input()) for i in range(n)]
i = s = 0
while i < n -1: # i chi can toi n-2
    j = i + 1
    while j < n:
        if a[i] == a[j] -1:
            s += 1
        j += 1
    i += 1
print("Ket qua: ",s)
"""
#C2:
"""
n = int(input(" Nhap so phan tu cua day: "))
print(" Nhap ",n, "phan tu: ")
a = [int(input()) for i in range(n) ]
kq = 0
dict1 = {}  
for j in range(n):  
    if dict1.get(a[j] -1) != None: 
        kq = kq + dict1[a[j] - 1]  
    if dict1.get(a[j]) == None:
        dict1[a[j]] = 1
    else:
        dict1[a[j]] = dict1[a[j]] + 1
print(" So cap so hang co gia tri lien tiep: ",kq)
"""

a = [] : se luu cac so nguyen
kq: đếm số cặp
dict1 : đếm tần suất xuất hiện
dict1[a[i]]: tan so xuat hien cua gia tri a[i]
a = [...]
Xet chi so thu a[j]
    b1. Tim gia tri phia sau: neu co thi
                            -> kq = kq + dict1[a[j] -1]
    b2. Cap nhat dict1 hien tai: neu khong co truoc do thi = 1 neu co thi
    cong them 1
#
n = int(input(" Nhap so phan tu cua day: "))
print(" Nhap ",n, "phan tu: ")
a = [int(input()) for i in range(n)]
kq = 0
dict1 = {}
for i in range(n):
    if dict1.get(a[i] - 1) != None:
        kq = kq + dict1[a[i]-1]
    if dict1.get(a[i]) == None:
        dict1[a[i]] = 1
    else:
        dict1[a[i]] += 1
print(" So cap so hang co gia tri lien tiep: ",kq)


































    
