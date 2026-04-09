t = int(input())

for _ in range(t):
    n = int(input())    #n is odd

    arr = [0, 1]
    for _ in range(n):
        a,b = map(int, input().split())
        arr.extend([a,b])

    if n <= 1:
        print(1)
        continue
    dictt = {}
    res = []

    for i in range(n*2, 0, -1):

        if arr[i] == 0:
            dictt[i] = 0
        else:
            res.append(i)

            if 2*i > 2*n:     #o day khong co con
                dictt[i] = 0
            else: #khong o day
                if arr[2*i] == 0:
                    dictt[i] = 0
                else:
                    dictt[i] = dictt.get(2*i, 0) + dictt.get(2*i+1, 0) + 4
      
    m = len(res)
    res = res[::-1]
    for j in res:
        if dictt[j] == 0:
            dictt[j] = dictt[j//2] + 1
            print(dictt[j//2] + 1, end = " ")
        else:
            if j > 1:
                dictt[j] = dictt[j//2] + dictt[j] +1
                
            else:
                dictt[j] += 1
            print(dictt[j], end = " ")
    print("")
    
