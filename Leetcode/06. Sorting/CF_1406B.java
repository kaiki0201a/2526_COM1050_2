import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class CF_1406B {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            long[] arr = new long[m];

            for (int k = 0; k < m; k++){
                arr[k] = Long.parseLong(st.nextToken());
            }

            Arrays.sort(arr);

            long ans_1 = arr[m-1]*arr[m-2]*arr[m-3]*arr[m-4]*arr[m-5];
            long ans_2 = arr[0]*arr[1]*arr[m-1]*arr[m-2]*arr[m-3];
            long ans_3 = arr[0]*arr[1]*arr[2]*arr[3]*arr[m-1];
            long ans = Math.max(Math.max(ans_1, ans_2),ans_3);

            sb.append(ans).append("\n");
        }

        System.out.println(sb.toString());
    }
}
