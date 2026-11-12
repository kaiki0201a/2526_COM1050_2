#Y tuong van la tim gap lon nhat giua cac hang rao
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def findlong(m, nums):
            sett = set()

            nums = [1] + nums + [m]
            checkset1 = set(nums)
            nums.sort()

            p = len(nums)

            #Lap 2 for tim gap
            for i in range(p):
                for j in range(i+1, p):
                    sett.add(nums[j]- nums[i])
            return sett
        
        res = -1

        nums1 = findlong(m, hFences)
        nums2 = findlong(n, vFences)
        
        hi = nums1.intersection(nums2)
        res = max(hi) if len(hi) > 0 else -1

        #Cach lau hon neu khong dung phep giao
        """
        for i in findlong(m, hFences):
            
            if i in findlong(n, vFences):
                res = max(res, i)
        """
        return res if res == -1 else res**2 %(10**9 + 7)
        
        

p1 = Solution()
print(p1.maximizeSquareArea(4,4,[2],[2,3]))