#Input:
n, l = map(int, input().split())    #So den long va do dai l

listt = list(map(int, input().split())) #Vi tri dat den long

#Y tuong: tim ban kinh be nhat co the, thi ta se tim ban kinh giua 2 bong den 
listt.sort()
n = len(listt)

i = 1
res = 0

while i < n:
    res = max(res, (listt[i] - listt[i-1])/2)
    i += 1
res = max(res, listt[0], l - listt[n-1])
print(res)

