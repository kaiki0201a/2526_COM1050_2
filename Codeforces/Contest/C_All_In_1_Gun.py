t = int(input())
#Dung prefix sum

for _ in range(t):

    n, h, k = map(int, input().split())
    arr = list(map(int, input().split()))

    res = [0]*(n+1)    #luu sat thuong
    for i in range(1,n+1):
        res[i] = arr[i-1] + res[i-1]

    minli = [0]*(n+1)   #luu gia tri nho nhat
    minva = float("inf")
    for i in range(n):
        if arr[i] < minva:
            minva = arr[i]
        minli[i+1] = minva
    
    maxli = [0]*(n+1) #luu gia tri lon nhat

    maxva = -float("inf")
    for i in range(n-1, -1, -1):
        if arr[i] > maxva:
            maxva = arr[i]
        maxli[i] = maxva

    total = res[n]

    solannap = h // total
    du = h % total
    maxli = [0] + maxli

    if du == 0:
        print((solannap - 1) * (n + k) + n) #khong tinh lan nap cuoi
        continue
    for i in range(1, n+1):
        if minli[i] < maxli[i+1]:
            res[i] = res[i] - minli[i] + maxli[i+1]
        if res[i] >= du:
            break
    print((k+n)*solannap + i)




    
