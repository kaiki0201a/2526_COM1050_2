t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = 2*s
    res = 0

    for i in range(n):
        count = 1
        for j in range(i+1, i+n):
            if s[j] != s[j-1]:
                count += 1
        res = max(res, count)
    print(res)


