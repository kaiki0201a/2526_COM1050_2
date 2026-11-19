import java.util.Arrays;

public class LC_2567_Minimum_Score_byC2 {
    public int minimizeSum(int[] nums) {
        if (nums.length < 4)
            return 0;
        Arrays.sort(nums);

        int min1 = Math.min(nums[nums.length - 2] - nums[1], nums[nums.length - 1] - nums[2]);
        min1 = Math.min(min1, nums[nums.length - 3] - nums[0]);

        return min1;
    }
}
