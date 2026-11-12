import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class C_1167_News_Distribution {
    static int[] UF;
    static int[] sz;

    // root
    public static int root(int i){
        if (i == UF[i]) return i;
        
        return UF[i] = root(UF[i]);
    }

    // union
    public static void union(int p, int q){
        int i = root(p);
        int j = root(q);

        if (i == j) return;

        if (sz[i] > sz[j]){
            UF[j] = i;
            sz[i] += sz[j];
        } else {
            UF[i] = j;
            sz[j] += sz[i];
        }
    }

    public static void main(String[] args) throws IOException{
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());   // Users
        int m = Integer.parseInt(st.nextToken());   // Groups Friends

        UF = new int[n+1];
        sz = new int[n+1];

        // Init 
        for (int i = 1; i < n+1; i++){
            UF[i] = i;
            sz[i] = 1;
        }

        for (int i = 0; i < m; i ++){
            st = new StringTokenizer(br.readLine());
            int number = Integer.parseInt(st.nextToken());
            if (number <= 1) continue;
            int u = Integer.parseInt(st.nextToken());

            for (int j = 1; j < number; j ++){
                int v = Integer.parseInt(st.nextToken());
                union(u, v);
            }
        }
        for (int i = 1; i < n + 1; i++) {
            sb.append(sz[root(i)]).append(" ");
        }
        System.out.println(sb.toString());
    }
    
}