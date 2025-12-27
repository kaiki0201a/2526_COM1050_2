class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        room_count = [0] * n
        #room end
        min_index_end = 0   #luu chi so
        room_end = [0]*n

        for i in meetings:
            count_free = False
            #Kiem tra phong free
            for j in range(n):
                #Neu phong day dang ban va gio hien tai da xong
                if i[0] >= room_end[j]:
                    #Cap nhat phong free
                    room_end[j] = 0
                    count_free = True
                    break
                
            #Cap nhat phong be nhat
            stt = min(room_end)
            min_index_end = room_end.index(stt)

            #Chen vao phong
            if count_free:  #Neu con phong
                #Them vao
                room_end[min_index_end] = i[1]
                
                #Cap nhat
                room_count[min_index_end] += 1

            else:   #Neu khong con thi chen vao phong gan het nhat
                #Chen vao va cap nhat
                room_end[min_index_end] = i[1] +(room_end[min_index_end] - i[0])
                room_count[min_index_end] += 1

        maxx = max(room_count)
        return room_count.index(maxx)


d1 = [[48,49],[22,30],[13,31],[31,46],[37,46],[32,36],[25,36],[49,50],[24,34],[6,41]]
print(mostBooked(4, d1))