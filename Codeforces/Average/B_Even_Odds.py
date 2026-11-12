a, b = map(int, input().split())

if a % 2 == 0:
    mid = a // 2

    if b > mid:
        print((b-mid)*2)
    else:
        print(b*2-1)
else:
    mid = a//2 + 1
    if b > mid:
        print((b-mid)*2)
    else:
        print(b*2-1)