class RecentCounter:

    def __init__(self):
        self.deque = []
    
    def ping(self, t: int) -> int:
        self.deque.append(t)    #Khi gap cuoc goi thi them no vao hangf doi

        #Khi no la cuoc goi khoi tao / khong thuoc [t-3000; t] thi pop
        # Vi so hang sau > so truoc nen viec ta xoa khong anh huong den viec dem cua so sau
        # Out 3000 so truoc => out 3000 so sau
        while self.deque[0] == [] or self.deque[0] < t - 3000:
            self.deque.pop(0)
        
        return len(self.deque)