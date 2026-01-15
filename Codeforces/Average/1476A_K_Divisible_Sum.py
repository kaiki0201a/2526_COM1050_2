#Cho n va k
#a1 + ... + an % k== 0. tim max an min

t = int(input())    #So test case

for i in range(t):
    n, k = map(int, input().split())

    #Neu k > n: ta se trai deu ra 
    if k > n:
        if k % n == 0:
            print(k//n)
        else:
            print(k//n + 1)
    #Neu n > k thi tung phan tu = 1 hoac 1 va 2 la thoa man dieu kien
    else:
        if n % k == 0:
            print(1)
        else:
            print(2)
