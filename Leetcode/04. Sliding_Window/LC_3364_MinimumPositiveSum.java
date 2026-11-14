import java.util.List;

public class LC_3364_MinimumPositiveSum {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int res = Integer.MAX_VALUE;

        for (int i = l; i <= r; i++){ // size
            int left = 0; int cur = 0;
            for (int right = 0; right < nums.size(); right++){
                cur += nums.get(right);
                if (right - left + 1 == i){
                    if (cur > 0){
                        res = Math.min(res, cur);
                    }
                    cur -= nums.get(left);
                    left++;
                }
            }
        }

        return (res != Integer.MAX_VALUE) ? res : -1;
    }
}
