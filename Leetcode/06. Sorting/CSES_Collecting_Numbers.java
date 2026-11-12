import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class CSES_Collecting_Numbers{
    public static int collectNumbers(int[] arr, int n){
        int count = 1;
        int[] col = new int[n+1];

        // Luu vi tri chinh xac cua i tren mang ban dau
        for (int i = 1; i <= n; i++){
            col[arr[i]] = i;
        }

        for(int i = 2; i <= n; i++){
            if (col[i-1] > col[i]){
                count += 1;
            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n+1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(collectNumbers(arr, n));

    }
}