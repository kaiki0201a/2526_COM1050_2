# Class gồm 2 thành phần chính: + Thuộc tính + Phương thức
# Định nghĩa một lớp:    class   <tên lớp>:
# Tạo một đối tượng kiểu lớp:   <tên đối tượng> = <Tên lớp>([các tham số])
# Hàm tạo của một lớp:
"""
    class < tên lớp >:
        def __init_(self, [ các tham số ]):
            [khối lệnh]
"""
# Cơ chế hoạt động của hàm tạo
"""
- Mỗi khi một đối tượng lớp được tạo ra, hàm tạo __init__() sẽ tự động thực hiện
"""
# Tham số self: sử dụng để tham chiếu đến tường đối tượng được tạo ra
# Thay đổi giá trị của các thuộc tính
"""<tên đối tượng>.<thuộc tính> = <giá trị mới>"""
# Xoá một đối tượng: del< tên đối tượng>
#-------------------#
#Vidu_lop_cha_con
"""
class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def infor(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
#Xay dung lop student
class student(person):
    def __init__(self, name, age, year):
        person.__init__(self, name, age)
        self.graduation = year
    def infor(self):
        person.infor(self)
        print("Graduation year: ",self.graduation)
p1 = student("Phan Xuan Vong", 35, 2000)
p1.infor()
"""
#Ham super(): thay vi phai viet ten lop thi ta co the dung super()
"""Tiep tuc vidu voi person va student:
Khi super().__init__() chạy, thì thiết lập p1.name, p1.age


#Thiet lap lop cha: person
class person():
    def __init__(self, name, age):  #Ham tu khoi tao
        self.name = name
        self.age = age
    def infor(self):    #Ham in ra
        print("Name: ",self.name)
        print("Age: ",self.age)
# Thiet lap lop con: student
class student(person):
    def __init_(self, name, age, year): #Ham tu khoi tao lop con co them thuoc tinh
        super().__init__(name, age) #Thay vi dung person.__init__(self,name,age)
        self.graduation = year
    def infor(self):
        super().infor()     #thay vi dung person.infor(self)
        print("Graduation year: ",self.graduation)
p1 = student("Phan Xuan Vong", 35, 2000)
p1.infor()
"""
#---------BT-------
#BT1. Lớp hình chữ nhật

class rectange:
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def chuvi(self):
        return 2 * (self.chieudai + self.chieurong)
    def dientich(self):
        return self.chieudai * self.chieurong

#BT2: Sap xep cac danh sach cac doi tuong hinh chu nhat
# A < B neu: Sa < Sb hoac Sa = Sb, Ca<Cb
class tinh(rectange):
    def __init__(self,chieudai, chieurong):
        super().__init__(chieudai, chieurong)
        self.chuvi = 2*(self.chieudai + self.chieurong)
        self.dientich = self.chieudai * self.chieurong
    def __lt__(self, other):
#C1.    return self.dientich < other.dientich or ( self.dientich == other.dientich and self.chuvi < other.chuvi)
        if self.dientich < other.dientich:
            return True
        if self.dientich == other.dientich and self.chuvi < other.chuvi:
            return True
        return False
    def infor(self):
        print("Dien tich la: ",self.dientich)
        print("Chu vi la: ",self.chuvi)
p1 = tinh(3,4)
p2 = tinh(4,5)
p3 = tinh(2,6)
ds = [p1, p2, p3]
ds.sort()
for x in ds:
    x.infor()

#BT3. To chuc loi giai theo lop
"""
    Cho day so ai(0-> n-1). Hay thuc hien cac cong viec.
    - Tinh tong cac phan tu cua day so
    - Tinh phan tu nho nhat
    - Tinh phan tu lon nhat
    - Dua ra tat cac cac bo hai phan tu co tong bang 0
"""

class dayso:
    def __init__(self, n):
        self.n = n
        self.a = [int(input()) for i in range(n)]
    def infor(self):
        for i in self.a:
            print(i, end = " ")
    def yeucau(self):
        print("Tong cac phan tu: ",sum(self.a))
        print("Phan tu be nhat: ",min(self.a))
        print("Phan tu lon nhat: ",max(self.a))
        s = []
        for i in self.a:
            if (-i,i) not in s and (i, -1) not in s:
                if self.a.count(-i) > 0:
                    b = [i, -i]
                    b.sort()
                    b = tuple(b)
                    s.append(b)
        print("Tat ca cac bo co tong bang 0: ")
        for i in s:
            print(i)
p1 = dayso(5)
p1.yeucau()

    
        
        
        






