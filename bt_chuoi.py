#Ly thuyet
#1. Tach chuoi:
    #<bc>.split(ki tu phan tach); mac dinh la white space
#2. Chuyen doi thuong hoa:
    #<bc>.upper, <bc>.lower
#3. Chuyen ki tu dau thanh in hoa:
    #<bc>.capitalize()
#4. Chuyen doi moi ki tu thanh in hoa:
    #<bc>.title()
#5. hoa-> thuong va nguoc lai:
    #<bc>.swapcase()
#6. Phep toan in: a in b-> dung tra ve true, sai thi false
#7. Dem so lan xuat hien:
    #<bc>.count<str1>; dem tu chi so i: <bc>.count(<str>,i,j)
#8. Phuong thuc tim kiem:
    #<bc>.find(str1); tra ve chi so dau tien
    #co the them tham so nhu #7
#9. Phuong phap thay the:
    #<bc>.replace(str_old, str_new)
    #co the them so chuoi toi da de thay: <bc>.replace(str_old, str_new)
#10. Phuong thuc xoa cac ki tu white space o ben trai, ben phai
    #<bc>.lstrip()
    #<bc>.rstrip()
    #<bc>.strip()
#11. Can chinh chuoi:
    # <bc>.ljust(width) : them ki tu trang vao ben phai sao cho do dai chuoi la width
    # <bc>.rjust(width)
    # <bc>.center(width)
    # Co the thay the white space: <bc>.___(width, "ki tu them vao ")
    # them ki tu 0 vao ben trai: <bc>.zfill(width)
#12. Mot so PT is___
    #12.1: <bc>.isdigit(): true neu chi chua ki tu chu so
    #12.2: <bc>.ispace(): true neu chi chua ki tu trang
    #12.3: <bc>.islower(): true neu cac ki tu chu thuong (so van thoa man)
    #12.4: <bc>.isupper(): true neu cac ki tu chu hoa (so van thoa man)
    #12.5: <bc>.isalpha(): true neu chi co chu cai thuong/hoa
    #12.6 <bc>.istitle()
#13. Ham max min tren chuoi:
    #min(<bc>); max(<bc>)
#14. Ham eval cho bt toan hoc:
    #eval(<bc>)
#15. Ham sorted(<>): sap xep theo thu tu tang dan tra ve 1 list
#16. PT: <str>.join(<...>) tra ve mot chuoi bang cach them cac phan tu <>
    #                           vao giua
#17.Ham ord(ch) : tra ve ma ki tu ch trong bang ma ASCII
#18.Ham chr(h) : tra ve ki tu trong bang ma ASCII co ma ki tu bang h
#-------------------------------------------------
#1.Dua ra cac tu trong chuoi phan cach boi dau, va white space:
"""Lap duoc ham chua chuoi va ngat ra khi du dk, hoac white space
    B1: tach tat ca cac ki tu ra
    B2: Gom tung ki tu neu gap , hoac thi k gom ma in ra
"""
"""
st = input(" Nhap chuoi bat ky: ")
st1 = st.split()
st2 = []
for x in st1:
    x= x.split(",")
    st2 = st2 + x
for x in st2:
    if x != "":
        print(x)
"""
#2. Tong cac chu so trong chuoi
""" B1: tim cac ki tu so
    B2:tinh
"""
"""
st = input(" Nhap chuoi can tinh toan: ")
n = len(st)
tong = 0
i = 0
while i < n:
    if "0" <= st[i] <= "9": #hoac co the dung if x.isdigit():
        tong = tong + int(st[i])
    i += 1
print(" Tong la: ",tong)
"""
#3. Chuoi hoan vi
"""dem tung ki tu
tinh toan tong
"""
"""
st1 = input(" Nhap chuoi thu nhat: ")
st2 = input(" Nhap chuoi thu hai: ")
n = len(st1)
b = "" # chuoi de xac dinh bat dau tu dau
k = 0 # tinh toan tong cac chi so
i = 0
while i < n:
    j= 0
    a = st1.find(st2[i]) #tim chi so dau tien
    while j<n:
        if (str(a) in b) == False: #dk rang chua xuat hien
            k = k + int(a)
            b = b + str(a)
            break
        else:
            a = st1.find(st2[i],a+1) #tim lap lai tu vi tri tiep theo
            j += 1    
    i += 1
d= n*(n-1)/2
print("d = ",d)
print("k = ",k)
if k == d:
    print(" Day la 2 chuoi hoan vi ")
else:
    print(" Day khong phai la 2 chuoi hoan vi ")
"""
# Cach 2: su dung ham sorted sap xep theo thu tu tang dan
"""
str1 = input(" Nhap chuoi 1: ")
str2 = input( " Nhap chuoi 2: ")
str1 =  "".join(sorted(str1)) #tra ve mot chuoi ki tu thay vi 1 list
str2 = "".join(sorted(str2))
print(str1)
print(str2)
if str1 == str2:
    print("true")
else: print("false")
"""
#4.Dat phep toan
# 2 vong lap
"""
a = input(" nhap vao chuoi so 1: ")
b = input(" nhap vao chuoi so 2: ")
n1 = len(a)
n2 = len(b)
i = 0
s = 0
while i < n1:
    k =eval( a[0:i] + "+ " + a[i: n1] ) #tach ra hai chuoi vao dung phep eval
    j = 0
    while j < n2:
        h =eval( b[0:j] + "+ " + b[j: n2] ) #tach ra hai chuoi va dung phep eval
        if h == k:
            print(h)
            s += 1
        j +=1
    i += 1
if s>= 1:
    print(" so cach dat la ",s)
else:
    print(" khong co cach dat ")
"""
#5. Mat ma Caesar
#Hint: Ham ord(ch) : tra ve ma ki tu ch trong bang ma ASCII
     # Ham chr(h) : tra ve ki tu trong bang ma ASCII co ma bang h
#Buoc1: Tim xem no o dau dau bang ma
# Buoc 2: dich chuyen
st1 = input(" Nhap chuoi can chuyen doi: ")
st2 = ""
for i in st1: #lap de xac dinh chuoi va tra ve
    h = ord(i)
    k = chr(h+2)
    st2 = st2 + k
print(st2)
    





























    
