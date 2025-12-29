#BT6: Bieu dien so
def dau_phay(x):
    n = len(str(x))
    h, k = n//3, n % 3
    if k == 0:
        return h-1
    else:
        return h
n = int(input("Nhap so n: "))
print("So dau phay can de ngan cach la: ", dau_phay(n))
