a, b, s = map(int, input().split())

h = s - (abs(a)+abs(b))
if h < 0:
    print("NO")
    exit(0)

if h % 2 == 0:
    print("YES")
else:
    print("NO")