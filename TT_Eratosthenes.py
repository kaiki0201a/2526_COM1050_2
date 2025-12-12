# Nếu muốn sàng các số nguyên tố không vượt qúa n
# Phải tạo 1 list có kich thước n+1 phần tử vi chi so duoc danh so tu 0
# Coi tất cả các số từ 0 tới n là số nguyên tố
# Xét list[i] = 1
# Xét list[i] = 0
# Xét từ i ta sẽ thay đổi list[i*k] = 0 với k = 1,2,3,...int(n/i)
# Một số không phải số nguyên tố thi chắc chắn có ước bé hơn hoặc bằng sqrt nó
# Vd khi xet den 30 ma can 30~5,4 nen xet den 5 la đủ
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
n = int(input("Nhap so can in ra: "))
def Era(n):

    #Set tat ca deu la so nguyen to:  1 la T; 0 la False, den n + 1 vi chi so bd tu 0
    
    list_a = [1] * (n+1)
    list_a[0], list_a[1] = 0, 0

    #Ktra tu 2
    p = 2
    while p*p <= n:
        if list_a[p] == 1:
            for i in range(p*p, n+1, p):
                list_a[i] = 0
        p += 1
    for j in range(2, n+1):
        if list_a[j] == 1:
            print(j, end = " ")
Era(n)



        
