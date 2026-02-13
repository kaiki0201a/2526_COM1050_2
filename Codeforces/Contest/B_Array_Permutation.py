#Hoan vi giu nguyen vi tri tuong doi ban dau -> dua ve bai toan tim chuoi con


t = int(input())

for _ in range(t):
    n = int(input())

    res = []
    per = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    for i in range(n):
        if not res:
            res.append(arr[i])
        elif arr[i] != res[-1]:
            res.append(arr[i])
    i, j = 0, 0
    m = len(res)
    while j < n:
        if res[i] == per[j]:
            i += 1
        if i == m:
            print("YES")
            break
        j += 1
        
    if i < m:
        print("NO")
            