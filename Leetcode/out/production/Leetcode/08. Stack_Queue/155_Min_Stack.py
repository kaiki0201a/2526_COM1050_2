#Stack already has pop(), peak(), push() but now we wanna getmin in O(1) time
#Hint: Consider each node in the stack having a minimum value
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        #Trong stack thi chi can them binh thuong
        self.stack.append(val)

        #Them gia tri be nhat tai diem do
        self.minstack.append(val if len(self.minstack) == 0 else min(val, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        #Cap nhat luon ca gia tri min sau khi xoa -> xoa pop min stack
        self.minstack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minstack[-1]

    