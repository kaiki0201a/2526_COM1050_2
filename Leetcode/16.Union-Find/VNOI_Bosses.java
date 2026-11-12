import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class VNOI_Bosses {
    static int[] UF;
    static int[] deepth;

    public static int root(int i){

        if (i == UF[i]) return i;
        // Tranh thu luc tim root thi hoan thi phan cong don

        int oldParent = UF[i];

        UF[i] = root(UF[i]);    // Thực hiện nối đến tổng

        deepth[i] += deepth[oldParent];

        return UF[i];
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        UF = new int[n+1];
        deepth = new int[n+1];

        // Init
        for ( int i = 1; i < n + 1; i++){
            UF[i] = i;
            deepth[i] = 0;
        }
        for (int i = 0; i < m; i ++){
            st = new StringTokenizer(br.readLine());
            String type = st.nextToken();
            int u = Integer.parseInt(st.nextToken());
            
            if (type.equals("1")){
                int v = Integer.parseInt(st.nextToken());
                UF[u] = v;
                deepth[u] = 1;
            } else {
                root(u);
                sb.append(deepth[u]).append("\n");
            }
        }
        System.out.println(sb.toString());
    }
}
