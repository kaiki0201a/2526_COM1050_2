"""
#Dieu kien de thoa man la so phan tu lap lai <= n^2 -n: khi do no co dang aii luon khac phan tu do
"""

t = int(input())
for i in range(t):
    n = int(input())
    res = - float("inf")
    dictt = {}

    for _ in range(n):
        arr = list(map(int, input().split()))
        for i in arr:
            dictt[i] = dictt.get(i, 0) + 1
            res = max(res, dictt[i])
    if n == 1:
        print("NO")
        continue
    if res > n**2 - n:
        print("NO")
    else:
        print("YES")

