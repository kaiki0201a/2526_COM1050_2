"""
- write: ghi một chuỗi kí tự vào tệp, không xuống dòng

- writelines(<một đối tượng>): Ghi nội dung một đối tượng vào tệp, nội dung
    phải là dãy kí tự
    
- read(): Đọc tất cả các kí tự trong tệp (kể cả kí tự xuống dòng) và lưu chúng
    thành một chuỗi kí tự
    
- read(n): Đọc n byte tính từ vị trí con trỏ tệp. Khi các kí tự được mã hoá
    theo bảng mã ASCII thì mỗi kí tự được tính là 1 byte

- readline(): Đọc từng dòng của tệp văn bản

- readlines(): Đọc cả tệp và lưu chúng thành một danh sách, mỗi phần tử của
    danh sách là một dòng (gồm cả kí tự xuống dòng)

- with open(<tên tệp>,'..') as <biến tệp>:
    <Khối lệnh làm việc với tệp>
"""
#BT1. Tổng các số hạng lẻ
"""
- Mở tệp Dayso.py để đọc dữ liệu
- Đọc dữ liệu của tệp theo từng dòng và lưu chúng dạng một chuỗi kí tự (readline)
- Thực hiện tách các số hạng trong chuỗi, mỗi số hạng tách được, nếu là
    số hạng lẻ thì cộng chúng vào tổng kết quả.
- Để tách các số hạng trong chuỗi ta dùng spilt(), ds nhận được gồm:
    số hạng, các kí tự trống, kí tự xuông dòng
"""
"""
f = open("bt_tep1.py",'r')   # Mo tep ... de doc
list_lines = f.readlines(); # doc tat ca, luu ve dang danh sach
print("Bieu dien: ",list_lines)
f.close()
kq = 0
for st in list_lines:
    list = st.split()
    print("A: ",list)
    for x in list:
        if x != '\n' and x != ' ':
            y = int(x)
            if y % 2 == 1:
                kq += y
print(" Tong cac so hang le: ",kq)
"""

#BT2. Phân loại dữ liệu
# Goi y dung alpha va digit, alpha la chu cai, digit la so
"""
    Ý tường thuật toán:
    Mở tệp dataa.tx để đọc dữ liệu tệp, 2 tệp còn lại để lưu kết quả
    - Đọc từng dòng trong tệp Data và xử lý đối với tưng dòng
        Với mỗi dòng:
    Tạo hai chuỗi alpha,digit để lưu dữ liệu trên dòng đang xử lý
    Xét từng kí tự trên một , nếu là latinh thì lưu vào alpha, so thi luu latin
    
"""
"""
f = open("bt_tep2.py", 'r')
f1 = open("latinh.pt",'w')
f2 = open("chuso.py", 'w')
list_lines = f.readlines();
print("Bieu dien: ",list_lines)
for x in list_lines:
    chu = ""
    so = ""
    print("X la:",x)
    for i in x:
        if i.isdigit() == True:
            so += i
        if i.isalpha() == True:
            chu += i
    if chu > "":
        f1.write(chu + "\n")
    if so > "":
        f2.write(so + "\n")
f.close()
f1.close()
f2.close()
"""

#Loi giai
"""
f = open("bt_tep2.py", 'r') #mo tep goc
so = open("chuso.py", 'w')  #tep luu chu so
latinh = open("latinh.py", 'w') #tep luu chu cai
read_lines = f.readlines()  #readlines: doc tat ca va tao thanh 1 list
print("Bieu dien: ",read_lines)
for st in read_lines:
    alpha = ""
    digit = ""
    print("ST la: ",st)
    for x in st:
        print("X la: ",x)
        if x.isdigit():
            digit += x
        if x.isalpha():
            alpha += x
    if alpha > "":
        latinh.write(alpha + '\n')
    if digit > "":
        so.write(digit + '\n')
f.close()
so.close()
latinh.close()
"""
#BT3. Rap phach
"""
- 3 tep du lieu:
    + Sbd_Ph : so bao danh va so phach
    + Sbd_Ten: so bao danh va ho ten
    + Ph_Diem: so phach va diem
- Rap thong tin: Sbd, ho ten, diem
    + Sap xep danh sach thi sinh nay theo diem giam dan va ghi du lieu ra tap kq

#Huong giai:
- Nhung tep nay lien ket voi nhau
B1. Noi 2 tep sbd_ph voi sbd_ten:
- Gia su dung tuple de luu
"""
"""
#Doc tep Sbd_ten va dua vao list
f1 = open("sbd_ten.py", 'r')
line1 = f1.readlines()
print(line1)
dict1 = {}  #list chua sbd va hoten
for i in line1:
    b = i.split()
    print(b)
    so = ""
    chu = ""
    for j in b:
        if j.isdigit():
            so += j
        if j.isalpha():
            chu = chu + j + " "
    sbd = hoten = ""
    if so > "":
        sbd = sbd + so
    if chu > "":
        hoten = hoten + chu
    dict1[sbd] = hoten
print("DICT 1: ",dict1)
#Doc du lieu tu tep ph_diem
print("-------------------")
f2 = open("ph_diem.py", 'r')
line2 = f2.readlines()
print("LINE2: ",line2)
dict2 = {}
list2 = []
for i in line2:
    b = i.split()
    print(b)
    list2.append(b)
print("list2: ",list2)
for i in range(len(list2)):
    dict2[list2[i][0]] = list2[i][1]
print("DICT2: ",dict2)
#Doc du lieu tu tep sbd_ph theo tung dong
print("----------")
f3 = open("sbd_ph.py", 'r')
list_kq = []
for i in range(len(list2)):
    row3= []
    line3 = f3.readline()
    print("LINE3: ",line3)
    b = line3.split()
    print(b)
    sbd = b[0]
    hoten = dict1[sbd]
    diem = dict2[b[1]]
    row3.append(int(diem))
    row3.append(hoten)
    row3.append(sbd)
    list_kq.append(row3)
print("---------")
print(list_kq)
list_kq.sort()
list_kq.reverse()
print("DAP AN: ")
for i in list_kq:
    print(i[::-1])
f1.close()
f2.close()
f3.close()
#BUOC1: Dua sbd_ph va sbd_ten vao dict
#BUOC2: Xet trong ph_diem va tao 1 list moi luu ket qua truy van tu dict1, dict2
#BUOC3: Sap xep: dung linh hoat giua sort va reverse
"""
#C2:
#Mo cac tep:
sbd_ph_file = open("sbd_ph.py", 'r')
sbd_ten_file = open("sbd_ten.py", 'r')
ph_diem_file = open("ph_diem.py", 'r')
ket_qua_file = open("dapan1.py", 'w')
#Doc du lieu tu cac tep
sbd_ph_lines = sbd_ph_file.readlines()
sbd_ten_lines = sbd_ten_file.readlines()
ph_diem_lines = ph_diem_file.readlines()
#Tao tu diem luu sbd - ten
sbd_ten_dict = {}
#Xet tung dong trong tep sbd_ph.py
for x in sbd_ten_lines:
    x.strip()
    list = x.split(' ',1)   #tach whitespace, tham so toi da la 1
    sbd = list[0].strip()
    ten = list[1].strip()
    sbd_ten_dict[sbd] = ten
#Tao tu diem luu ph_diem
ph_diem_dict = {}
#Xet tung dong trong tep ph_diem
for x in ph_diem_lines:
    x.strip()
    list = x.split()
    phach = list[0].strip()
    diem = list[1].strip()
    ph_diem_dict[phach] = diem
#Tien hanh rap phach
list_kq = []
#Xet tung dong trong tep sbd_ph
for x in sbd_ph_lines:
    x.strip()
    list = x.split()
    sbd = list[0].strip()
    phach = list[1].strip()
    #Chuyen sang kieu du lieu int de sap xep
    diem = int(ph_diem_dict[phach])
    ten = sbd_ten_dict[sbd]
    list_kq.append((diem, ten, sbd))
#Sap xep danh sach hoc sinh theo diem giam dan
list_kq.sort(reverse = True) #xep theo chieu giam dan
#Ghi ket qua ra tep dapan1.py
for x in list_kq:
    line = x[2] + ': ' + x[1] + ':' + str(x[0])
    ket_qua_file.write(line)
    ket_qua_file.write('\n')
#Dong cac tep da mo
sbd_ph_file.close()
sbd_ten_file.close()
ph_diem_file.close()
ket_qua_file.close()
    
    











                
