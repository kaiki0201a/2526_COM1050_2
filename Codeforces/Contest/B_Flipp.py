t = int(input())

#Nhan xet neu 0: le, 1: chan thi co the swap duoc
for _ in range(t):

    n = int(input())
    s = input()

    h, k = 0, 0  #h: 0, k:1

    res1 = []
    res2 = []
    for i in range(n):
        if s[i] == "1":
            k += 1
            res1.append(i)
        else:
            h += 1
            res2.append(i)        
    if k % 2 == 0:
        print(len(res1))
        for i in res1:
            print(i+1, end = " ")
        print()
    elif h % 2 != 0:
        print(len(res2))
        for i in res2:
            print(i+1, end = " ")
        print()
    else:
        print(-1)
