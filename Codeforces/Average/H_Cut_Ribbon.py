listt = list(map(int, input().split()))
res = listt[1:]
n = listt[0]
res.sort()
a = res[0]
b = res[1]
c = res[2]

for i in range(0, n//c+ 1):

    for j in range(0, n//b + 1):

        for k in range(0, n//a + 1):

            if i*c + j*b + k*a == n:
                print(i+j+k)
                exit(0)