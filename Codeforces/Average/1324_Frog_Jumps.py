n = int(input())    #The numbers of the test case

for i in range(n):
    arr = input()
    k = len(arr) + 1 #Ô cần đến

    arr = listt(arr)
    arr = ["R"] + arr

    step = int(k**2)    #Bien dem

    if step ** 2 < k:
        step += 1
    
    left, right = 0, 1

    while right < k:
        if arr[right] == "R":
            step = max(step, right - left)

            left = right

        right += 1

    print(step)



