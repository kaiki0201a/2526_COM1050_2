#Ý nghĩa: Dùng 2 stack tạo thành 1 queue
#Y tuong:
#stack 1: lưu đúng chiều            #1 2 3 4 5
#stack 2: lưu theo chiều ngược lại  #5 4 3 2 1
#Neu queue la 12345 thi push la push vao stack1, pop = pop tu stack 2


class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:     #Khong tra ve gi chi them vao
        #Push vao stack 1
        self.s1.append(x)

    def pop(self) -> int:

        #B1. Dao nguoc
        #Một list rỗng được xem là False nhưng s1 = [] khác s1 = None
        if not self.s2: #Khi s2 = []; if not s2 : if True
            while self.s1:  #khi s1 != []
                self.s2.append(self.s1.pop())
        #B2. Lay ra tu stack 2
        return self.s2.pop()
            
    #peek tuong tu pop nhung khong lam mat gia tri
    def peek(self) -> int:
        if not self.s2:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())

        x = self.s2.pop()
        self.s2.append(x)
        return x

    def empty(self) -> bool:
        return len(self.s1) + len(self.s2) == 0
            
        
