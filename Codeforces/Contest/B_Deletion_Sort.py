t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    sw = True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            sw = False
            break
    if sw:
        print(n)
    else:
        print(1)