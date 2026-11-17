import java.util.Stack;

public class LC_2243_Calculate_Digit_Sum {
    public String digitSum(String s, int k) {
        StringBuilder sb = new StringBuilder(s);
        int length;
        while (sb.length() > k){
            StringBuilder next = new StringBuilder();

            int val = sb.length();
            for (int i = 0; i < val; i += k){
                int cur = 0; int j = 0;
                for (j = 0; sb.length() > 0 && j < k; j++){
                    cur += Integer.parseInt(sb.substring(j, j+1));
                }
                sb.delete(0, j);
                next.append(cur);
            }
            sb.append(next);
        }
        return sb.toString();
    }
}
