def team(n):
    count = 0

    for i in range(n):
        arr = list(map(int, input().split()))
        if sum(arr) >= 2:
            count += 1
    
    return count
n = int(input())
print(team(n))