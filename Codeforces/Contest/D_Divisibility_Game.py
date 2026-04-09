import math

t = int(input())
for _ in range(t):
    h, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    n = len(a)
    leng = len(b)

    m = a[0]
    maxx = max(b)
    for i in range(1,n):
        m = math.lcm(m, a[i])
        if m > maxx:
            break

    Ga, Gb, Gc = 0, 0, 0
    for j in b:
        if j % m == 0:
            Ga += 1
    listt = [1] + [0]*maxx

    set_a = set(a)
    for i in set_a:
        j = 1
        while i*j <= maxx:
            if listt[i*j] == 0:
                listt[i*j] = 1
            j += 1
    
    for i in b:
        if listt[i] == 0:
            Gb += 1
    Gc = leng - Ga - Gb

    if Ga + (Gc % 2) > Gb:
        print("Alice")
    else:
        print("Bob")