t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = set(arr)
    if 67 in arr:
        print("YES")
    else:
        print("NO")