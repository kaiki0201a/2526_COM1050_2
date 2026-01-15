s = input()

l = 0
res = 1

for r in range(1,len(s)):

    if s[r] != s[l]:

        res = max(res, r-l)
        l = r
    if res >= 7:
        print("YES")
        exit(0)

if s[r] == s[l]:
    res = max(res, r-l+1)
if res >= 7:
    print("YES")
else:
    print("NO")

