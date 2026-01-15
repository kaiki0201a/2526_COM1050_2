#Two team
#So luong bang nhau, 1 team la doc nhat, 1 team la giong nhau
from collections import Counter
t = int(input())    #So test case

for i in range(t):
    n = int(input())    #So luong hoc sinh o moi test case

    listt = list(map(int, input().split()))
    dictt = {}

    maxx = 0    #Luu ki nang xuat hien nhieu nhat
    for i in listt:

        if i in dictt:
            dictt[i] += 1
        else:
            dictt[i] = 1
        maxx = max(dictt[i], maxx)
    
    #Neu ki nang xuat hien nhieu nhat = so luong ki nang
    if maxx == len(dictt):
        print(len(dictt)-1)
    
    #Neu ki nang xuat hien nhieu nhat > so luong ki nang
    elif maxx > len(dictt):
        print(len(dictt))

    #Neu ki nang xuat hien nhieu nhat < so luong ki nang
    else:
        print(maxx)
