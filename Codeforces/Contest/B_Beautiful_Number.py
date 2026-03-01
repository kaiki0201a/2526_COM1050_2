t = int(input())
for _ in range(t):

    x = int(input())
    x = str(x)

    n = len(x)

    if n <= 0:
        print(0)
        continue

    listt = []

    res = 0

    total = 0
    for i in x:
        listt.append(int(i))
        total += int(i)
    listt.sort()

    if total < 10:
        print(0)
        continue

    sw = True
    for i in range(n-1, -1, -1):
        if listt[i] < int(x[0]) and sw:
            total += 1
            sw = False
        if total >= 10:
            total = total - listt[i]
            res += 1
        else:
            break
    print(res)
        
    
