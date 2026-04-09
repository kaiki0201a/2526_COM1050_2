s, n = map(int, input().split())

res = []
for i in range(n):
    res.append(list(map(int, input().split())))

res.sort()

i = 0

while i < n:
    a = res[i][0]
    b = res[i][1]

    if s > a:
        s += b
    else:
        print("NO")
        exit(0)
    i += 1
print("YES")

