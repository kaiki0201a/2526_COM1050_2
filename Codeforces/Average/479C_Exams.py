#Ca ngay thi thuc te va ngay thi chinh thuc phai sap xep khong giam
n = int(input())    #So ngay se thi

res = []
for i in range(n):
    listt = list(map(int, input().split()))
    res.append(listt)

res.sort()

i = 1
cur = res[0][1]

#So sanh voi ngay thi truoc, neu duoc thi som thi thi khong thi phai thi dung
while i < n:
    if res[i][1] < cur:
        cur = res[i][0]
    else:
        cur = res[i][1]
    i += 1

print(cur)
