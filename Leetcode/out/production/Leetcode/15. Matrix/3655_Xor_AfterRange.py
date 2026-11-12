class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
    # Threshold for square root decomposition
        B = 300 
    
    # Final multiplier for each index
        multipliers = [1] * n
    
    # Group small-k queries to process them efficiently
        small_k_queries = [[] for _ in range(B + 1)]
        large_k_queries = []
    
        for l, r, k, v in queries:
            if k > B:
                large_k_queries.append((l, r, k, v))
            else:
                small_k_queries[k].append((l, r, v))
            
    # 1. Process Large k Queries (Direct Simulation)
    # Total complexity: O(Q * N/B)
        for l, r, k, v in large_k_queries:
            for i in range(l, r + 1, k):
                multipliers[i] = (multipliers[i] * v) % MOD
            
    # 2. Process Small k Queries (Difference Array / Prefix Products)
    # Total complexity: O(B * N)
        for k in range(1, B + 1):
            if not small_k_queries[k]:
                continue
            
        # diff array stores multiplicative changes
            diff = [1] * (n + k)
        
        # Cache modular inverses to avoid repeated pow() calls
            inv_cache = {}
        
            for l, r, v in small_k_queries[k]:
                if v not in inv_cache:
                    inv_cache[v] = pow(v, MOD - 2, MOD)
                inv_v = inv_cache[v]
            
            # Start of the progression
                diff[l] = (diff[l] * v) % MOD
            
            # Find the last index in the range [l, r] that belongs to this progression
                num_steps = (r - l) // k
                last_idx = l + num_steps * k
            
            # End of the progression (one step after last_idx)
                if last_idx + k < n + k:
                    diff[last_idx + k] = (diff[last_idx + k] * inv_v) % MOD
        
        # Calculate prefix products with step k to find total multiplier per index
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i-k]) % MOD
                multipliers[i] = (multipliers[i] * diff[i]) % MOD
            
    # 3. Calculate final XOR sum
        ans = 0
        for i in range(n):
            final_val = (nums[i] * multipliers[i]) % MOD
            ans ^= final_val
        
        return ans