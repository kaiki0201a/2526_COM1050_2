# Tach ki tu so va ki tu chu cai
"""
a=""
b=""
c=""
str=str(input(" nhap vao chuoi bat ki: "))
n=len(str)
for i in range(n):
    if "0" <= str[i] <= "9":
        a=a + str[i]
    elif "a" <= str[i] <= "z":
        b=b + str[i]
    elif "A"<= str[i] <= "Z":
        c= c + str[i]
print(a)
print(b)
print(c)
"""
#Chuoi doi xung
"""
str=str(input(" nhap vao chuoi bat ki: "))
str2=str[::-1]
if str2==str:
    print(" Day la chuoi doi xung ")
else:
    print(" Day khong phai la chuoi doi xung")
"""
#Nen chuoi
"""
chuoi = str(input(" Nhap vao chuoi bat ky "))
a = ""
i= 0
n= len(chuoi)
h=1
while i<n:           #i se chay tu 0-> n-1
    j=i                 # tao j de batdau xet tu vi tri thu j
    k=1                  #dem so lan lap lai
    a= a + chuoi[i]         # in ra moi gia tri bat dau
    while j<n-1:    #n-1 vi n thi ngoai range
        if chuoi[j] == chuoi[j+1]:
            k=k+1
        else:
            break #pha chuoi chay lai tu dau
        if k>=2:
            a= a+ str(k)
        j=j+1
    i=i+k
print(a)
"""
#giai nen chuoi
#Buoc1:tim vi tri chuoi can giai nen bang 1 vong lap
            #
#Buoc2: Xac dinh so can giai nen, dung lenh if va elif de xac dinh khi can xac dinh nhieu so lien ke
#Buoc3: giai nen va lap lai

str1 = input(" Nhap chuoi can giai nen: ")
chuoi = ""
n = len(str1)
so = ""
i=0
while i < n: #chay den ki tu thu n-1: chuan
    if "0" <= str1[i] <= "9":
        so = so + str1[i]
    elif so = "":
        chuoi = chuoi + str1[i]
    else:
        chuoi = chuoi + str1[i] * int(so)
        so = ""
    i += 1
print(" Chuoi sau khi giai nen la: ",chuoi)
"""
str2 = input(" Nhap xau de giai nen: ")
str1 = "" #
so_ = "" #
n = len(str2)
i=n-1 #dk vong lap
while i>=0:
    if "0" <= str2[i] <= "9": # xac dinh so lan lap
        so_ = str2[i] + so_ #
        print(so_)
    elif so_ == "":
        str1 = str2[i] +str1 #them vao chu cai tu sau dem lai
    else:
        str1 = str2[i] * int(so_) + str1 # giai nen chuoi
        so_ = ""
    i=i-1
print(" Chuoi giai nen: ",str1)
"""
#Mat khau
#c1
"""
mk = input( "Nhap mat khau: ")
n = len(mk)
for i in range(n):
    for h in range(0,n-i+1):
        so=thuong=hoa=0
        if i+h<n:
            for j in range(h,i+h+1):
                if "0" <= mk[j] <= "9":
                    so=1
                if "a" <= mk[j] <= "z":
                    thuong=1
                if "A" <= mk[j] <= "Z":
                    hoa=1
            if so==thuong==hoa==1:
                print(" Mat khau thoa man la", mk[j-i:j+1])
                quit()
"""
#c2 mk
"""
str1 = input( " Nhap chuoi str1 de tim chuoi mat khau: ")
n = len(str1)
index_hoa = index_thuong = index_so = -1
a=n 
for i in range(n): #chay tung ki tu trong str1
    if "0" <= str1[i] <= "9": 
        index_so = i #gan i la vi tri xuat hien so
    elif "a" <= str1[i] <= "z":
        index_thuong = i # gan i la vi tri xuat hien chu thuong
    else:
        index_hoa = i #gan i la vi tri xuat hien chu hoa
    t = min(index_hoa, index_thuong, index_so) # t la vi tri xuat hien dau tien
    if -1 < t and i - t +1 <=a: #-1 < t: da co bo thoa man, i la bo xuat hien cuoi cung, t la bo xuat hien dau tien i - t +1 la do dai chuoi<n
        b = t
        a = i - t + 1 # gan a la do dai xau
print(" Chuoi mat khau: ",str1[b:b+a])
"""


















    
    
