"""
#Du lieu hang doi - queue
    - La danh sach cac phan tu
    - Gom 2 phep toan co ban: put - get; thuc hien tai 2 dau
    - First In First Out: Vao truoc ra truoc
#Du lieu ngan xep - stack
    - La danh sach cac phan tu
    - Gom 2 phep toan co ban: put - get; thuc hien tai 1 dau
    - Last In First Out: Vao sau ra truoc
    - Phan tu duoc them vao sau cung dgl phan tu o dinh danh sach (top)
#Du lieu hang doi 2 dau - deque
    - La danh sach cac phan tu
    - Ho tro 2 phep toan co ban: them(append) va lay ra(pop)
    - Hai phep toan duoc thuc hien tai ca 2 dau danh sach
    - append(x) them phan tu vao dau ben phai
    - pop() lay phan tu o dau ben phai
    - appendleft(x) them phan tu x vao dau ben trai
    - popleft() lay phan tu o dau ben trai
#Hang doi uu tien - Priority queue
    - La danh sach cac phan tu
    - Moi phan tu co the so sanh duoc
    - Phan tu a .nho hon. phan tu b thi ta noi a co .uu tien. < b
    - Hang doi uu tien ho tro 2 phep toan co ban: + Them 1 phan tu
                                            + Lay ra phan tu co uu tien be nhat
    - Hang doi uu tien thuong duoc to chuc theo cau truc heap
    - Cac phep toan them va lay ra deu co do phuoc tap O(log2n); n la so phan tu
    trong hang doi
"""
#queue: queue.Queue(), put, get, empty, full, qsize: Vao truoc ra truoc
#stack: queue.LifoQueue(), put, get, empty, full, qsize: Vao sau ra truoc
#deque: queue.deque(), append, pop, extend, len: Vao sau ra truoc
#Priority: queue.PriorityQueue(), put, get, empty:
"""
import sys, os, argparse, queue
class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self,other):
        if self.x + self.y > other.x + other.y: #Neu cai nay dung thi self, other
            return True
        if self.x + self.y == other.x + other.y:
            return self.x > self.y
    def Print(self):
        print((self.x, self.y))
my_priority = queue.PriorityQueue()
my_priority.put(point(8, 10))
my_priority.put(point(10, 8))
my_priority.put(point(10, 10))
my_priority.put(point(11, 2))
while not my_priority.empty():
    x = my_priority.get()
    x.Print()
"""
#-------------
#BT1.Tim so
"""
Cho k chu so khac nhau va 2 so nguyen duong M1, M2. Hay su dung cac chu
so trong k chu so de ghep thanh X thoa man:
X chia het cho M1: la boi so
X <= M2
X la so nho nhat co the
Mot chu so co the dung nhieu lan
- Xet tu so co 1 chu so-> 2 chu so-> n chu so; n = len(M2)
+ Voi truong hop co 1 chu so=> se la ai
+ Voi truong hop co 2 chu so; aiai; aiaj; aiak; ajai; ajaj;ajak
"""

#Ham de quy liet ke tat ca cac so co the co, tu 1 bo so
#So ki tu toi da se la len(M2)
"""
M1 = int(input("Nhap so M1 de tim kiem: "))
M2 = int(input("Nhap can tren de xac dinh: "))
print("So ki tu toi da: ", len(str(M2)))    #So ki tu toi da khi xet, 1,2,3,4
n2 = int(input("Nhap so chu so ban dau: ")) #n2 de xac dinh k
k = [int(input()) for i in range(n2)]   # k la cac gia tri co the nhan
k.sort()
print("K la: ",k)
#De quy co nho ban dau set 1 list x= [0]
# Voi tung j thi se la so cac chu so
def lietke(i):
    for a in k: #nhan gia tri
        x[i] = a
        if  i == j-1:
            print(x)
            s = " "
            for h in x:
                s = s + str(h)
            print("S la: ",int(s))
            if 0 < int(s) <= M2:
                if int(s) % M1 == 0:
                    print("So do la: ",int(s))
                    exit()
            elif int(s)>0:
                print("Khong co so ton tai ")
                exit()
        else:
            lietke(i+1)
for j in range(1, len(str(M2)) +1): #so ki tu
    x = [0 for i in range(j)]   # x day 
    lietke(0)
    print("HET HANG: ",j)
"""
#C2:
"""NX:
x la so duoc lay ra
so moi duoc tao thanh: x* 10 + a[i]
"""
"""
import sys, os, argparse, queue
#Khoi tao hang doi va du lieu ban dau
my_queue = queue.Queue()
k = int(input("Nhap so chu so: "))
M1 = int(input("Nhap M1: "))
M2 = int(input("Nhap M2: "))
print("Nhap",k,"chu so khac nhau: ")
#Khoi tao danh sach chua gia tri
a = [int(input()) for i in range(k)]
a.sort()
if a[0] == 0:
    X = 0
    print("So can tim: ",X)
    exit(0)     #exit(0) co nghia la ct da chay dung
#Them phan tu 1 chu so
for x in a:
    my_queue.put(x)
while not my_queue.empty():
    x = my_queue.get()
    if x % M1 == 0 and x <= M2:
        X = x
        print("So can tim: ",X)
        exit(0)
    for t in a:
        u = x * 10 + t;
        if u <= M2:
            my_queue.put(u)
print("Khong co X")
"""
#BT2: Ma di tuan nhanh nhat
#C1
"""
import sys, os, argparse, queue
#Khoi tao ban dau
my_queue = queue.Queue()
new_queue = queue.Queue()
print("Nhap toa do ban dau: ")
b = [int(input()) for i in range(2)]    #b la gia tri diem bat dau
print("Nhap toa do diem den: ")
b1 = [int(input()) for i in range(2)]

m = int(input("Nhap so dong: "))
n = int(input("Nhap so cot: "))
m = m-1
n = n-1
#Khoi tao danh sach gia tri
c = [-1, 1]
d = [-2, 2]
a = []
for i in range(2):
    row1 = []
    row1.append(c[i])
    for j in range(2):
        row1.append(d[j])
        row2 = row1[::-1]
        a.append(row1[:])   #Them vao ban sao
        a.append(row2[:])
        del row1[1]
print("Cac gia tri co the nhan la: ")
a.sort()
print(a)
my_queue.put(b) #Buoc dau tien
def kiemtra(queue, j, new_queue):
    if j <= m + n:
        while not queue.empty():
            x = queue.get()
            if x == b1:
                print("So buoc di can it nhat la: ",j)
                exit(0)
            else:   #Khoi tao buoc di moi
                for i in range(8):
                    moi = []
                    moi1 = x[0] + a[i][0]
                    moi2 = x[1] + a[i][1]
                    if 0 <= moi1 <= m and 0 <= moi2 <= n:
                        moi.append(moi1)
                        moi.append(moi2)
                        new_queue.put(moi)
        else:
            print("Khong co duong di")
            exit(0)
    kiemtra(new_queue, j+1, queue)
#Tao ra queue moi
kiemtra(my_queue, 0, new_queue)
print("Khong di chuyen duoc")
"""
#C2
"""
import sys, os, argparse, queue
my_queue = queue.Queue()
def Inboard(i, j):
    if 0 <= i < m and 0 <= j < n:
        return True
    else:
        return False
m = int(input("Nhap so dong m <=1000: "))
n = int(input("Nhap so cot n <= 1000: "))
x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
u = int(input("Nhap u: "))
v = int(input("Nhap v: "))
if (x, y) == (u, v):
    print("Khong can di chuyen!")
    exit(0)
drow = [-1, -1, 1, 1, -2, -2, 2, 2]
dcol = [-2, 2, -2, 2, -1, 1, -1, 1]
d = [[0 for i in range(n)] for j in range(m)]   #Tao bo nho
my_queue.put((x,y))
while not my_queue.empty() and d[u][v] == 0:    #d[u][v] = 0 => chua den duoc
    (xt, yt) = my_queue.get()   #lay ra gia tri
    for t in range(8):
        i = xt + drow[t]
        j = yt + dcol[t]
        if not Inboard(i, j): continue  #Neu khong nam trong board thi xoay
        if (i, j) != (x,y) and d[i][j] == 0:
            d[i][j] = d[xt][yt] + 1
            my_queue.put((i, j))
if d[u][v] == 0:
    print("Khong di chuyen duoc. ")
else:
    print("So buoc di chuyen it nhat: ",d[u][v])
"""
#BT3. Chuoi ngoac dung
"""
chuoi = str(input("Nhap chuoi ngoac: "))
i, j = 0, 0
n = len(chuoi)
for t in chuoi:
    if i >= j:
        if t == "(":
            i += 1
        else: j+= 1
    else:
        print("Khong phai chuoi dung!")
        exit(0)
if i==j:
    print("La chuoi dung!")
else:
    print("Khong phai chuoi dung!")
"""
#C2
"""
import sys, os, argparse, queue
chuoi = str(input("Nhap chuoi ngoac: "))
my_queue = queue.Queue()
for i in chuoi:
    if i == "(":
        my_queue.put(i)
    elif i == ")":
        if not my_queue.empty():
            my_queue.get()
        else:
            print("Khong phai chuoi dung!")
            exit(0)
if my_queue.empty():
    print("La chuoi dung")
else:
    print("Khong phai chuoi dung!")
"""
#BT4. Bac cua chuoi ngoac dung. La so ngoac mo ton tai nhieu nhat
"""
import sys, os, argparse, queue
my_stack = queue.LifoQueue()
str = input("Nhap chuoi ngoac dung: ")
deg = 0
for x in str:
    if x == "("):
        my_stack.put(x)
        deg = max(deg, my_stack.qsize())
    else:
        my_stack.get()
print("Bac cua chuoi bang: ",deg)
"""
#BT5: Xoa k chu so
import sys, os, argparse, queue
#C1
"""
#Tim chu so lon nhat, roi tim so thu 2, thu 3

def hamtimchuso(a, k):
    vi_tri, gia_tri =0, 0
    n = len(a)
    if k!= 0:
        for i in range(0, n - k + 1):
            if a[i] > gia_tri:
                gia_tri = a[i]
                vi_tri = i
        print(gia_tri, end= "")
    a = a[vi_tri+1:]
    if k == 0:
        print("\nDa xong!")
        exit(0)
    else:
        hamtimchuso(a,k-1)
#Khoi tao danh danh a
x = int(input("Nhap so tu nhien: "))
a = []
n = len(str(x))
for i in str(x):
    a.append(int(i))

k = int(input("Nhap chu so can xoa di: "))
print("So chu so con lai la: ",n -k)
#st nay dung de luu chi so
hamtimchuso(a,n - k)
"""
#C2. Dung stack: ( queue.lifoqueue())
"""
#Khoi tao x va stack
x = int(input("Nhap so tu nhien X: "))
my_queue = queue.LifoQueue()

n = len(str(x))
print("So chu so ban dau la: ",n)
k = int(input("Nhap chu so can xoa di: "))
print("So chu so con lai la: ",n-k)

b = str(x)
for i in range(n):
    while k > 0 and not my_queue.empty():
        top = my_queue.get()
        if int(b[i]) >= top:
            k = k -1
        else:
            my_queue.put(top)
            break
    my_queue.put(int(b[i]))
    
while k > 0:
    my_queue.get()
    k = k - 1

xnew = ""
while not my_queue.empty():
    p = my_queue.get()
    xnew = xnew + str(p)

xnew = xnew[::-1]
print("So sau khi xoa la: ",int(xnew))
"""
#BT6. Gia tri lon nhat trong doan gom k so hang lien tiep cua day so
import sys, os, argparse, queue
#C1
"""
#Nhap vao day so
n = int(input("Nhap so so hang cua day: "))
a = [int(input()) for i in range(n)]
print("Day do la: ", a)
k = int(input("So so hang cua day con la: "))

#Tao stack
st = []

#Tao thu cong voi 3 so dau
for i in range(k):
    while len(st) != 0:
        if a[i] > st[-1]:
            st.pop()
            continue
        else:
            st.append(a[i])
            break
    st.append(a[i])
print("So lon nhat trong chuoi 1: ",st[0])

#Tu so thu 4:
for i in range(k,n):
    while len(st) != 0:
        if a[i] > st[-1]:
            st.pop()
            continue
        else: break
    st.append(a[i])
    print(f"Check chuoi voi i la {i} ",st)
    if len(st) >= k:
        del st[0]
    print(f"So lon nhat trong chuoi {i-1} la: ",st[0])
"""
#C2
"""
import sys, os, argparse, queue
my_deque = queue.deque()
#Phan khai bao
n = int(input("Nhap n = "))
k = int(input("Nhap k = "))
print("Nhap",n,"phan tu: "))
a = [int(input()) for i in range(n)]

#Xu ly
# x trong my_deque gom (i,a[i]) luu vi tri va gia tri
for i in range(k):
    while len(my_deque) > 0:
        x = my_deque.pop()
        if x[1] > a[i]:
            my_deque.append(x)
            break;
        my_deque.append((i,a[i]))
print(my_deque[0][1])
#

for i in range(k, n):
    while len(my_deque) > 0:
        x = my_deque.pop()
        if x[1] > a[i]:
            my_deque.append(x)
            break;
    my_deque.append((i,a[i]))
    while my_deque[0][0] <= i - k:  #chi so be nhat phai la i -k +1; chi so cuoi la i
        my_deque.popledt()
    print(my_deque[0][1])
"""
#BT7. Tro choi Bo vao - Lay ra
"""
import sys, os, argparse, queue
#Khoi tao
n = int(input("Nhap so so hang cua danh sach: "))
S = [int(input()) for i in range(n)]
my_pri = queue.PriorityQueue()
for i in S:
    my_pri.put(i)
k = int(input("Nhap so luoi choi: "))
print("CHECK S: ",S)

#Xu ly
for i in range(k):
    x = my_pri.get()
    print(f"So lay ra trong lan choi thu {i+1} la: ",x)
    my_pri.put(2*x)
"""
#BT8. Truy van trung vi
"""
import sys, os, argparse, queue
#Se dung 2 pri de luu min va max voi trung vi la gia tri nho nhat cua max

#Khoi tao
a = [int(input()) for i in range(1)]
print("Trung vi thu nhat la :",a[0])
min_pri = queue.PriorityQueue()
max_pri = queue.PriorityQueue()
max_pri.put(a[0])

#
k = int(input("So lan them: "))
for i in range(k):
    print("Lan them thu: ",i)
    x = int(input())
    y = int(input())
    #B1. Them vao: ( vao min put -; vao duong put +)
    q_value = max_pri.get()
    if x >= q_value:
        max_pri.put(x)
    else:
        min_pri.put(-x)
    if y >= q_value:
        max_pri.put(y)
    else:
        min_pri.put(-y)
    max_pri.put(q_value)

    #B2: Can bang
    n, m = min_pri.qsize(), max_pri.qsize()
    h = m - n
    if h == -1:
        min_get = min_pri.get()
        max_pri.put(-min_get)
    if h == 3:
        max_get = max_pri.get()
        min_pri.put(-max_get)
    q_value = max_pri.get()
    print(f"Trung vi sau lan them thu {i} la: ",q_value)
    max_pri.put(q_value)
"""
#C2.
import sys, os, argparse, queue
MinPriorityQueue = queue.PriorityQueue()
MaxPriorityQueue = queue.PriorityQueue()
a_0 = int(input("Nhap a_0 = "))
MaxPriorityQueue.put(-a_0)
n = int(input("Nhap so lan thuc hien: "))
a_i = -MaxPriority.get()
for i in range(1,n+1):
    x = int(input("x = "))
    y = int(input("y = "))
    MinPriorityQueue.put(x)
    MinPriorityQueue.put(y)
    MinPriorityQueue.put(a_i)
    u = MinPriorityQueue.get()
    v = MinPriorityQueue.get()
    MaxPriorityQueue.put(-u)
    MaxPriorityQueue.put(-v)
    a_i = -MaxPriorityQueue.get()
    print("Trung vi lan",i,"bang: ",a_i)
    
    
        
















