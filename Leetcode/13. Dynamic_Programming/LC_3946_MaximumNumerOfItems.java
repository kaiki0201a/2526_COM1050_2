import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LC_3946_MaximumNumerOfItems {
    public int maximumSaleItems(int[][] items, int budget) {
        int n = items.length;

        int[] bonus = new int[n];
        for (int i = 0; i < n; i++){
            int fI = items[i][0];
            for (int j = 0; j < n; j++){
                if (i != j && items[j][0] % fI == 0)
                    bonus[i]++;
            }
        }

        int totalSteps = 2 * n;
        int[][] dp = new int[2 * n + 1][budget + 1];
        for (int[] row: dp){
            Arrays.fill(row, -1);
        }

        dp[0][0] = 0;

        for (int i = 0; i < n; i++){
            int price = items[i][1];
            int firstGain = 1 + bonus[i];

            // Mua lan dau
            int stepFirst = 2 * i + 1;
            for (int b = 0; b <= budget; b++){
                dp[stepFirst][b] = dp[stepFirst - 1][b];

                if (b >= price && dp[stepFirst -1][b - price] != -1){
                    dp[stepFirst][b] = Math.max(
                            dp[stepFirst][b],
                            dp[stepFirst - 1][b - price] + firstGain
                    );
                }
            }

            // Buoc 2: Mua them cac ban sau khi da kich hoat (+1 moi lan, lay tu chinh hang hien tai)
            int stepExtra = 2 * i + 2;
            for (int b = 0; b <= budget; b++){
                dp[stepExtra][b] = dp[stepExtra -1][b];
                if (b >= price && dp[stepExtra][b - price] != -1){
                    dp[stepExtra][b] = Math.max(
                            dp[stepExtra][b],
                            dp[stepExtra][b - price] + 1
                    );
                }
            }

        }

        int ans = 0;
        for (int b = 0; b <= budget; b++){
            ans = Math.max(ans, dp[totalSteps][b]);
        }

        return ans;

    }
}
