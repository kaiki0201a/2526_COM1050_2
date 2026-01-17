#C1:
class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        res = 0
        while i < n:

            res += 1

            if i + nums[i] >= n -1:
                return res

            #Tai moi cho chon node de lan sau nhay xa nhat
            cur_reach, id_reach = 0, 0
            for j in range(i+1, i + nums[i]+ 1):
                if j + nums[j] > cur_reach:
                    cur_reach = j + nums[j]
                    id_reach = j

            print(id_reach)
            i = id_reach

#C2:
class Solution2:
    def jump(self, nums: List[int]) -> int:
        most_far = 0
        jump = 0
        end = 0

        n = len(nums)

        for i in range(n-1):
            most_far = max(most_far, i+nums[i])

            if i == end:

                jump += 1
                end = most_far

                if end >= n-1:
                    break
            
        return jump
            



p1 = Solution()
print(p1.jump([2,3,1,1,4]))

