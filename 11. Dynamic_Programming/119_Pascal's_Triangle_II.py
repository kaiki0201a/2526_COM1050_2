#C1:
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums = [1]

        i = 0
        while i < rowIndex:     #Xay tung hang, voi rowindex = 0 => nums =[1]
            #Xay thu cong 2 dau va o giua thi 
            row = [1]

            j = 0
            while j < len(nums) - 1:
                k = nums[j] + nums[j+1]
                row.append(k)
                j+=1
            
            row += [1]
            nums = row
            i += 1
            
        return nums
    
    
#C2: Moi vi tri se nhan 2 gia tri
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        res = [1]

        for i in range(rowIndex):
            #Xay dung row moi
            next_row = [0] *((len(res)) + 1)
            for j in range(len(res)):
                #Them vao tung o se duoc nhan gia tri
                next_row[j] += res[j]
                next_row[j+1] += res[j]

            res = next_row
        return res
        
        
