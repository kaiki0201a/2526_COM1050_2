#Key va lambda
"""
sinh_vien = [('An', 20), ('Bình', 18), ('Châu', 22)]

# Sử dụng lambda cho tham số key
sinh_vien.sort(key=lambda phan_tu: phan_tu[1])

print(sinh_vien)
# Kết quả: [('Bình', 18), ('An', 20), ('Châu', 22)]
"""
#BT1: Viet chuong trinh con tim gia tri lon nhat cua 2 so, 3 so, n so
    # 2 so
"""
def lonnhat2(a,b):
    return max(a,b)
a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))
print("So lon hon la: ",lonnhat2(a,b))
"""
    # n so
"""
def max_list(x, *L):
    kq = x
    for y in L:
        if y > kq: kq = y
    return kq
print(max_list(0, *[1,2,3]))
"""
#BT2: Fibonacci
"""
def fi(n):
    if n < 1:
        return "So hang thu n phai lon hon 1"
    if n == 1:
        return 1
    if n > 1:
        b = c = 1
        for i in range(n-2):    #them n - 2 so tru hai so dau
            b, c = c, b + c
        return c
n = int(input("Nhap so hang can in ra: "))
print(fi(n))
"""
#BT3:Tam giac Pascal
#C1
"""
print("Tam giac pascal gom n + 1 dong: ")
n = int(input("Nhap n: "))
def pasca(n):
    global b
    if n < 0: #n = 0 -> so dong la 1
        return "So dong cua tam giac Pascal phai lon hon 1"
    if n == 0:
        return print(1)
    if n >= 1:   #co it nhat 2 dong
        print(1)
        print(1, 1,end = " ")
        print("")
        j = 1   #so phan tu se them
        b = [1, 1]
        while j < n: #them n - 1 so, , hang tiep theo them 1, xong them 2...
            c = b   #c de luu bien b hang i-1
            b = [1]     #reset b de them vao
            for i in range(1, 1 + j):   # 2,3,...
                k = c[i-1] + c[i]
                b.append(k)
            b.append(1)
            for h in b:
                print(h, end = " ")
            print("")
            j += 1
pasca(n)
print("-----------")
"""
#C2:
#Ham de in ra cac phan tu trong danh sach
def printlist(L):
    for x in L:
        print(x, end = " ")
    print()
#--
def pascal(n):
    list1 = [1] #danh sach cap nhat
    d = 0
    while d <= n:   #0,1 ,...n -> n + 1 dong
        printlist(list1)    #in thu cong dong 1
        list2 = [] + list1      #list nay dung de luu dong phia tren
        for i in range(len(list1) - 1):     # len list1 -1: so phan tu se them
            list1[i+1] = list2[i+1] + list2[i]
        list1 = list1 + [1]
        d += 1
#BT4. Viết chương trình con tham số vào là một dãy số và trả về kết qủa
#   là một dãy số đại diện(mỗi phần tử chỉ xuất hiện một lần)
"""
def taodanhsach(n):
    global a
    print("Nhap phan tu: ")
    a = [int(input()) for i in range(n)]
    return a
def rutgon(a):
    a1 = set(a)
    a2 = list(a1)
    return a2
n = int(input("Nhap so phan tu cua danh sach: "))
print(taodanhsach(n))
print("Danh sach rut gon la: ",rutgon(a))
"""
#BT5. Tham so la cac chuong trinh con
#sum_square(<bien kieu danh sach>): tra ve tong binh phuong
"""
def taodanhsach(n):
    global a
    print("Nhap phan tu: ")
    a = [int(input()) for i in range(n)]
    return " "
def sum_square(a):
    s = 0
    for i in a:
        s = s + i**2
    return s
def sum_cube(a):
    s = 0
    for i in a:
        s = s + i**3
    return s
n = int(input("Nhap so phan tu cua danh sach: "))
print(taodanhsach(n))
def sum_function(f, a):
    return f(a)
print("Tong binh phuong la: ")
print(sum_function(sum_square, a))
print("Tong lap phuong la: ")
print(sum_function(sum_cube, a))
"""
        
            










            
