t = int(input())
for _ in range(t):
    n, m, d = map(int, input().split())

    leng = d//m + 1
    if leng == 1:
        print(n)
        continue
    if n <= leng:
        print(1)
        continue
    if n % leng == 0:
        print(n//leng)
    else:
        print(n//leng + 1)