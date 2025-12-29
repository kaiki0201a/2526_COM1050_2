#BT4: Phan tich thanh tong 3 so lien tiep
def phan_tich(n):
    if n % 3 == 0:
        a = n//3
        return f"{n} = {a-1} + {a} + {a+1}"
    else:
        return "Khong the phan tich"
"""
n = int(input("Nhap so can xet: "))
print(phan_tich(n))
"""
