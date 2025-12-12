"""
def count_words(sentence: str) -> int:
    return len(sentence.split())
"""
"""
def count_words(sentence: str) -> int:
    if sentence == "":
        return 0
    return len([t for t in sentence.split(" ") if t != ""])
"""
"""
def count_words(sentence: str) -> int:
    return len(sentence.strip().split())
print(count_words("  hi\nlo ban  "))
"""
# Task B — Loops
"""
- 2TH:
 +) TH1. Neu a[j] < a[i] thi cac phan tu sau se khong can xet a[j] nua
     => xoa a[j]
     + TH2. Neu a[j] > a[i]: luu lai va a[j] chinh la chi so can tim
"""
#Tim lon nhat gan nhat ve phia ben trai
"""
def process(a):
    n = len(a)
    st = []     #luu chi 
    for i in range(n):
        while len(st) != 0 and a[st[-1]] <= a[i]: #phan tu cuoi cua st la chi so
            st.pop()
        ans = -1
        if len(st) != 0:
            ans = st[-1]
        print(ans, end = " ")
        st.append(i)

a = [2, 1, 4, 3]
process(a)
"""
#Tim be nhat gan nhat ve phia ben trai:
"""
def minleft(a):
    n = len(a)
    st = []
    c = []
    for i in range(n):
        while st and a[st[-1]] >= a[i]:
            st.pop()
        ans = -1
        if st:
            ans = st[-1]
        c.append(ans)
        st.append(i)
    print(c)
#Tim be hon gan nhat ve phia ben phai:
print("Chuoi ben phai: ")
def minright(a):
    n = len(a)
    b = []
    st = []
    for i in range(n-1,-1, -1):
        while st and a[st[-1]] >= a[i]:
            st.pop()
        ans = -1
        if st:
            ans = st[-1]
        b.append(ans)
        st.append(i)
    b = b[::-1]
    print(b)
a = [2, 1, 4, 3]
minleft(a)
minright(a)
# Tim hinh chu nhat:
"""
#TDTT
#1.List of dict
def main_list_of_dicts():
    # Khoi tao danh sach chua cac tu dien
    classroom_data = []

    while True:
        print("\n--- QUAN LY LOP HOC (List of Dictionaries) ---")
        print("1. Them hoc sinh")
        print("2. Tim kiem theo ID")
        print("3. Hien thi tat ca diem so")
        print("4. Thoat")
        choice = input("Chon yeu cau cua ban: ")

        if choice == "1":
            # a. Add a new student
            s_id = input("Nhap ID: ")
            s_name = input("Nhap ten: ")
            s_score = float(input("Nhap diem: "))

            # Tao dictionary cho hoc sinh nay va them vao list
            student_record = { "id": s_id, "name": s_name, "score": s_score}
            classroom_data.append(student_record)
            print("Da them thanh cong!")

        elif choice == "2":
            # b. Search by student ID
            search_id = input("Nhap ID can tim: ")
            found = False
            for student in classroom_data:      #duyet qua tung dict
                if student["id"] == search_id:
                    print(f"Tim thay: Ten: {student["name"]}, Diem: {student["score"]}")
                    found = True
                    break
            if not found:
                print("Khong tim thay hoc sinh nay. ")
        elif choice == "3":
            # c. Display all scores
            print("\n--- DANH SACH DIEM ---")
            for student in classroom_data:
                print(f"ID: {student["id"]}  |  Ten: {student["name"]}  |  Diem: {student["score"]}")

        elif choice == "4":
            break
        else:
            print("Lua chon khong hop le, hay nhap lai lua chon (1-4)! ")
main_list_of_dicts()
#2.Dict of list
def main_dict_of_list():
    # Khoi tao danh sach dict
    classroom_data = {}

    while True:
        print("\n--- QUAN LY LOP HOC (Dict Of List) ---")
        print("1. Them hoc sinh")
        print("2. Tim kiem theo ID")
        print("3. Hien thi tat ca diem so")
        print("4. Thoat")
        choice = input("Chon yeu cau cua ban: ")

        if choice == "1":
            # a. Add a new student
            s_id = input("Nhap ID: ")

            # Dam bao rang id chua ton tai
            if s_id in classroom_data:
                print("ID nay da ton tai! Vui long nhap ID khac. ")
                continue

            s_name = input("Nhap ten: ")
            s_score = float(input("Nhap diem: "))

            #Tao list de them hoc sinh nay vao voi key la ID
            classroom_data[s_id] = [s_name, s_score]
            print("Da them thanh cong!")

        elif choice == "2":
            #b. Tim kiem theo ID
            search_id = input("Nhap id can tim kiem: ")
            if search_id in classroom_data:
                print(f"ID: {search_id}  |   Ten: {classroom_data[search_id][0]}  |  Diem: {classroom_data[search_id][1]} ")
            else:
                print("Khong tim thay ID nay!")
            
        elif choice == "3":
            #c. Display all
            print("\n--- DANH SACH DIEM ---")
            for stu_id in classroom_data:
                print(f"ID: {stu_id}  |  Ten: {classroom_data[stu_id][0]}  |  Diem: {classroom_data[stu_id][1]} ")


        elif choice == "4":
            break

        else:
            print("Lua chon khong hop le, hay nhap lai lua chon (1-4)! ")
main_dict_of_list()  
        
        
                    










































