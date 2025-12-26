 
def bestClosingTime( customers: str) -> int:
    n = len(customers)
    listt1 = [0]*(n+1) # Store not come before i hour
    listt2 = [0]*(n+1)  #Store come after i hour

    i = 1   #hour
    while i < n+1:  #1-> n: because when i = 0: listt1[0] = 0
        #Count N before i hour
        if customers[i-1] == "N":
            listt1[i] = listt1[i-1] + 1
        else:
            listt1[i] = listt1[i-1]
            
        j = n - i   #0 -> n-1: because when i = n: listt2[n] = 0
        #Count Y after i hour
        if customers[j] == "Y":
            listt2[j] = listt2[j+1] + 1
        else:
            listt2[j] = listt2[j+1]
            
        i += 1
    
    print(listt1)
    print(listt2)
    pen = n

    for i in range(n+1):
        pen = min(pen, listt1[i]+ listt2[i])
        
    print("Res",pen)
strr = input()
bestClosingTime(strr)