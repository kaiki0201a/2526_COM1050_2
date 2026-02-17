t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 1:
        print(0)
        continue
    if n== 2:
        print(arr[1], arr[0])
        continue

    T = (arr[0] + arr[n-1])//(n-1)
    S1 = (arr[1] - arr[0] +T)//2
    print(S1, end = " ")

    for i in range(1,n-1):
        S = (arr[i+1] - arr[i] +T)//2
        print(S-S1, end = " ")
        S1 = S
    print(T- S1)
