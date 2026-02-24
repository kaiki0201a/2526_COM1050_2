t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x - 2*y < 0:
        print("NO")
        continue
    if (x - 2*y) % 3 != 0:
        print("NO")
        continue
    if x - 2*y < 6*-y:
        print("NO")
        continue
    print("YES")