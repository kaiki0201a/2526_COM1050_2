t = int(input())    #So test case

for _ in range(t):
    x = int(input())    #Gia tri dau vao

    count = 0
    for i in range(x+1, x + 90):
        y = sum(int(d) for d in str(i))
        if i - y == x:
            count += 1
    
    print(count)
