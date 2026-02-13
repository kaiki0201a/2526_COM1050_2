t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))

    new_arr = []
    for i in range(n):
        if arr[i] <= n:
            new_arr.append((arr[i], i))

    new_arr.sort()

    m = len(new_arr)
    count = 0
    for i in range(m):

        x , y = new_arr[i]  #x la gia tri

        if x*x > n or x > n:
            break
        for j in range(i+1, m):
            a, b = new_arr[j]

            if a * x > n or a > n:
                break
            elif a * x == abs(b - y):
                count += 1
    
    print(count)

