#Cho n vecto trong Oxyz, tinh tong xem = 0 hay khong

x, y ,z = 0, 0, 0
n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    x += a
    y += b
    z += c
if x == y == z == 0:
    print("YES")
else:
    print("NO")