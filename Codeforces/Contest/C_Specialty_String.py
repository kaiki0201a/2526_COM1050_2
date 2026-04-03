t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    arr = []
    i = 0
    while i < n:
        if not arr:
            arr.append(s[i])
        else:
            if s[i] == arr[-1]:
                arr.pop()
            else:
                arr.append(s[i])
        i += 1
    if arr:
        print("NO")
    else:
        print("YES")