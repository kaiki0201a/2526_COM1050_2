/*
a * b = lcm(a,b) * gcd(a, b);
Mở rộng ra n số chỉ đúng khi các số đôi một nguyên tố cùng nhau.
 */

import java.util.ArrayList;
import java.util.List;


public class LC_3411_MaximumSubarray {
    public int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public int maxLength(int[] nums) {
        int res = 2;
        int left = 0;

        for (int i = 1; i < nums.length; i++){
            int newt = left;
            for (int j = left; j < i; j++ ){
                if (gcd(nums[i], nums[j]) > 1){
                    newt = j + 1;
                }
            }

            res = Math.max(res, i - newt + 1);
            left = newt;
        }

        return res;
    }
}
