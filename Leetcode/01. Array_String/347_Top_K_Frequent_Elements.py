
#C1: Dung dict va sort
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Check voi base case
        if len(nums) <= 1:
            return nums
        if k > len(nums):
            return list(set(nums))


        dictt = Counter(nums)   #Tao dictt de dem so lan xuat hien

        res = []
        for ind, val in dictt.items():
            res.append([ind, val])  #Them vao gia tri va so lan xuat hien
        res.sort(key = lambda x: x[1])  #Sort theo so lan xuat hien

        i = len(res) - k    #Lay k phan tu xuat hien nhieu nhat

        cur_res = []    #Bien luu ket qua
        while i < len(res):
            cur_res.append(res[i][0])   #Them ket qua vao
            i += 1

        return cur_res
    
#C2:Dung heap va counter
import heapq
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = Counter(nums)

        heap = []
        for val, count in dictt.items():
            heapq.heappush(heap, (-count, val))  
        
        res = []
        for i in range(k):
            a, b = heapq.heappop(heap)
            res.append(b)
        
        return res

#C3: Toi uu hon khong can dung max heap
import heapq
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = Counter(nums)

        heap = []
        for val, count in dictt.items():
            heapq.heappush(heap, (count, val))  
        
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for i, num in heap]
p1 = Solution3()
print(p1.topKFrequent([4,1,-1,2,-1,2,3], 2))