import java.util.HashMap;

public class test {
    public int longestMonotonicSubarray(int[] nums) {
        int maxL = Integer.MIN_VALUE;
        int minL = Integer.MIN_VALUE;
        int curMax = 1;
        int curMin = 1;
        int res = 1;
        for (int i = 1; i < nums.length; i ++){
            if (nums[i] == nums[i-1]) {
                curMax = 1;
                curMin = 1;
            } else if (nums[i] > nums[i-1]) {
                curMax++;
                curMin = 1;
            } else {
                curMin++;
                curMax = 1;
            }

            maxL = Math.max(curMax, maxL);
            minL = Math.max(curMin, minL);
            res = Math.max(res, maxL);
            res = Math.max(res, minL);
        }

        return res;
    }
}
