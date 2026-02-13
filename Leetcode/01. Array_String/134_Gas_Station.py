class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)

        i = 0   #Started gas

        while i < n:
            
            j = i
            step = 0
            cur_gas = 0
            while step < n+1:
                cur_gas += gas[j]

                if j < n-1:
                    cost_gas = cost[j]
                    j += 1
                elif j == n -1:
                    cost_gas = cost[j]
                    j = 0
                print("CHECK: ", i, j, cur_gas, cost_gas, step)
                if cur_gas >= cost_gas:
                    cur_gas -= cost_gas
                    step += 1      
                else:
                    cur_gas -= cost_gas
                    break

            if step >= n and cur_gas >= 0:
                return i
            i += 1
        return -1

p1 = Solution()
print(p1.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))