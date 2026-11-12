l, r = map(int, input().split())

m = len(str(r))
res = []
sol = []

def backtracking():
    if len(sol) == n+1:
        res.append(sol[:])
        return
    for j in [4,7]:

        sol.append(str(j))
        backtracking()
        sol.pop()
for n in range(0,m+1):
    backtracking()

res_new = []
for i in res:
    b = "".join(i)
    res_new.append(int(b))



cur = 0
for i in res_new:

    while i >= l and l <= r:
        cur += i
        l += 1

print(cur)





