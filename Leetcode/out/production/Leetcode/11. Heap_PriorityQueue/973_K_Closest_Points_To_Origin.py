import heapq

#C1:Tao mot class de so sanh
class Poi:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x ** 2 + self.y **2 < other.x**2 + other.y**2:
            return True
        else:
            return False
    
    def infor(self):
        return [self.x, self.y]

class Solution:
    def kClosest(self, points: List[List[int]], k: int):
        heap = []

        for i in points:
            heapq.heappush(heap, Poi(i[0], i[1]))
        
        res = []
        for i in range(k):
            head = heapq.heappop(heap)
            res.append(head.infor())
        
        return res


#C2:Tao them mot phan tu la khoang cach ban dau de so sanh
class Solution2:
    def kClosest(self, points: List[List[int]], k: int):
        min_heap = [(x**2 + y**2, x, y) for x, y in points]

        heapq.heapify(min_heap)

        res = []

        for _ in range(k):
            x, y = heapq.heappop(min_heap)[1:]
            res.append([x, y])
        
        return res

points = [[1,3],[-2,2]]
p1 = Solution2()
print(p1.kClosest(points, 1))
