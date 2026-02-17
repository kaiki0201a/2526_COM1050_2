t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    i = 1
    while i < n:
        if arr[i] == 7- arr[i-1] or arr[i] == arr[i-1]:
            count += 1
            i += 2
        else:
            i+= 1

    print(count)