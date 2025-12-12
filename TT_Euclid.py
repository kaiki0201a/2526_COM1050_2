#Thuat toan dung de tim UCLN
""" Gia su can tim UCLN cua (a,b)
    Gia su a>b va UCLN=d
    <=> a = b.q +r, ma a chia het cho d
                        b chia het cho d=> r chia het cho d
            Hay UCLN(a,b)=UCLN(b,r)
"""
"""
a = int(input(" Nhap so tu nhien a "))
b = int(input(" Nhap so tu nhien b "))
h= min(a,b)
k = max(a,b)
r=0
i=1
while i>0:
    if k%h !=0:
        r=k%h
        k=h
        h=r
    else:
        print(" UCLN: ",h)
        break
    i=i+1
print(" BCNN", a*b/h)
"""
def ucln(a,b):
    while b>0:
        a, b = b, a%b
    return a
a = int(input())
b = int(input())
print(ucln(a,b))
