def countNegatives( grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0
    print("M: ",m)
    print("N: ",n)

    i, j = 0, 0
    while j < m:    #Kiem Tra tren tung dong
        if i < n:   #Tren tung dong kiem tra tung chi so

            #Neu tim ra so am:
            if grid[j][i] < 0:
                count += (n-i)
                i = 0
                print("Front")
            
            #Neu khong thi
            else:
                i += 1
                print("After")
                continue
        else:   #DK dung chuyen qua dong moi
            i = 0
        j += 1
        
    return count
print(countNegatives([[7, -3]]))