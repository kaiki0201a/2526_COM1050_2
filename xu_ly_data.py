#------
# PHẦN BÊN NGOÀI:Định nghĩa chức năng ( Thư viện )
#-------
"""
#Ham 1: Dinh nghia  logic tinh thue
def tinh_thue(gia, thue_suat):
    so_tien_thue = gia * thue_suat
    return so_tien_thue
#Ham 2: Dinh nghia logic tinh gia cuoi cung:
def tinh_gia_cuoi(gia_goc, thue_suat):
    thue = tinh_thue(gia_goc, thue_suat)    #Goi ra thue
    gia_cuoi = gia_goc + thue
    return gia_cuoi

#----Phan ben trong
if __name__ == "__main__":
    #1. Khoi tao du lieu dau vao (Bien, khong phai la tham so)
    GIA_SAN_PHAM = 1000
    THUE_SUAT = 0.10

    #2. Thuc hien LOI GOI HAM (Function call)
    gia_phai_tra = tinh_gia_cuoi(GIA_SAN_PHAM, THUE_SUAT)

    #3. Hien thi ket qua
    thue = tinh_thue(GIA_SAN_PHAM, THUE_SUAT)

    print("-- CHUONG TRINH TINH GIA SAN PHAM --")
    print(f"Gia goc san pham: {GIA_SAN_PHAM} dong")
    print(f"Thue suat ap dung: {THUE_SUAT * 100} %")
    print(f"So tien thue: {thue} dong")
    print(f"Gia cuoi cung phai tra: {gia_phai_tra} dong")
"""
"""
#Tan suat cua xau
def count_all(x):
    list_check = {}
    for char in x:
        if char in list_check:
            list_check[char] += 1
        else:
            list_check[char] = 1
    return list_check
#Dem xuat hien nhieu nhat
def count_max(x):
    list1 = {}
    for char in x:
        if char in list1:
            list1[char] += 1
        else:
            list1[char] = 1
    himax = 0
    ky = ""
    print(list1)
    for i in list1:
        if list1[i] >= himax:
            himax = list1[i]
            ky = i
    return f"Ky tu xuat hien nhieu nhat la {ky} voi ts la {list1[ky]}"
x = input()
print(count_max(x))
"""
"""
x = input("Nhap xau: ")
print("Tan suat la: ")
print(count_all(x))
"""
"""
#Luy thua cua 2
def check(n):
    if n < 2:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n //2
    return True
"""

def dem_so(n):
    ans = 0
    while n >= 5:
        n //=5
        ans += n
    return ans
n = int(input())
print(f"So 0 tan cung trong {n}! la: ",dem_0(n))








