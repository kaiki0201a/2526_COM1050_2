/*
y tuong: Dung prefix sum
Nhung thay vi tra loi cau hoi prefixSum[right] - prefixSum[left-1] = K
Ta se tra loi cau hoi prefixSum[right] - K = prefixSum[left-1]
 */

import java.util.HashMap;
import java.util.Map;

public class LC_560_SubarraySumEQK {


    public int subarraySum(int[] nums, int k) {
        int prefixSum = 0;
        int count = 0;

        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);

        for (int i = 0; i < nums.length; i++){
            prefixSum += nums[i];

            if (map.containsKey(prefixSum - k)) {
                count += map.get(prefixSum - k);
            }
            map.put(prefixSum, map.getOrDefault(prefixSum, 0) + 1);
        }
        return count;
    }

}
