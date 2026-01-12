#Xac dinh xem phai so gan may man hay khong
#So may man: chi gom 4 ,7

dictt = [4, 7, 47, 74, 474, 444, 447, 744, 747, 447]
n = int(input())
for i in dictt:
    if n % i == 0:
        print("YES")
        exit(0)

print("No")