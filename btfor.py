#tim tong so chu so cua n, tim tu hang don vi->bien doi hang chuc thanh hang dvi
"""n = int(input(" Nhap so tu nhien n "))
s=0
while n >0:
        s = s + n%10
        n = n//10
print(" Tong cac chu so cua n bang: ",s)
"""
#tim chu so lon nhat va chu so nho nhat
"""
n= int(input(" Nhap so tu nhien n "))
min_n=9
max_n=0
a=0
b=0
while n>0:
        a= n%10
        b= n%10
        n = n//10
        if a < min_n:
                min_n=a
                print(min_n)
                
        if b> max_n:
                max_n=b
                print(max_n)
print(" Chu so nho nhat la: ",min_n)
print(" Chu so lon nhat la: ",max_n)
"""
#Uoc chung lon nhat va boi chung nho nhat
"""
a= int(input(" Nhap so nguyen duong a: "))
b= int(input(" Nhap so nguyen duong b: "))
UCLN=0
BCNN=0
for i in range(1,max(a,b)+1):
        if a%i==0 and b%i==0:
                UCLN=i
for j in range(max(a,b),a*b+1):
        if j%a==0 and j%b==0:
                BCNN=j
                break
print(" BCNN cua ",a, "va",b, "la: ",BCNN)
print(" UCLN cua ",a, "va",b, "la: ",UCLN)
"""
#Kiem tra so nguyen to
"""
n= int(input(" Nhap so tu nhien n: "))
s=0
for i in range(1,n+1):
        if n%i==0:
                s=s+1
if s==2:
        print(n, " la so nguyen to")
else:
        print(n, " khong phai la so nguyen to ")
"""
#So hoan hao
"""
for i in range(1,10001):
        s=0
        for j in range(1,i+1):
                if i%j==0:
                        s=s+j
        if s== 2*i:
                print(i, " la so hoan hao ")
"""
#So luy thua 2-3
"""
n=int(input(" nhap so nguyen duong n: "))
h=-1
k=-1
i=0
while n %(2**i)==0:
        k=k+1
        i= i+1
print(n, "co phan tu 2 mu: ", k)
j=0
while n%(3**j)==0:
        h=h+1
        j=j+1
print(n," co phan tu 3 mu ",h)
s=0
d=(2**k)*(3**h)
p= n/d
if p==1 and n!=1:
        print(n, " la so luy thuy 2-3")
else:
        print(n, "khong phai la so luy thua 2-3 ")
"""









        
        
        

