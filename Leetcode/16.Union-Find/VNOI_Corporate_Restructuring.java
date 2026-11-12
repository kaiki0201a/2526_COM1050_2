// Y tuong: dung 2 DSU; mot cai cho su ket noi; mot cai kiem tra bo lien tiep gan nhau
// Ket hop giua Graph DSU va 1D DSU

import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.io.InputStreamReader;

public class VNOI_Corporate_Restructuring {
    static int[] UF;
    static int[] sz;
    static int[] DD_UF;

    public static int root(int i){
        if (i == UF[i]) return i;
        return UF[i] = root(UF[i]);
    }

    public static int findRoot2(int i){
        if (i == DD_UF[i]) {
            return i;
        }
        return DD_UF[i] = findRoot2(DD_UF[i]);
    }

    public static void union_1(int u, int v){
        int i = root(u);
        int j = root(v);
        if ( i == j) return;

        if (sz[j] > sz[i]){
            int temp = i;
            i = j;
            j = temp;
        }

        UF[j] = i;
        sz[i] += sz[j];
    }

    // Tim kiem diem dich moi, dap di cai da noi
    public static void union_2(int u, int v){
        int i = findRoot2(u);
        while (i < v){
            union_1(i, i + 1);
            DD_UF[i] = i + 1;   
            i = findRoot2(i);
        }

    }
    public static boolean connected(int u, int v){
        return root(u) == root(v);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        UF = new int[n+1];
        sz = new int[n+1];
        DD_UF = new int[n+1];

        for (int i = 1; i < n + 1; i ++) {
            UF[i] = i;
            sz[i] = 1;
            DD_UF[i] = i;
        }

        for (int i = 0; i < q; i++){
            st = new StringTokenizer(br.readLine());

            String type = st.nextToken();
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            if (type.equals("1")){
                union_1(u, v);  
            } else if (type.equals("2")){
                union_2(u, v);  
            } else if (connected(u, v))
                sb.append("YES").append("\n");
            else
                sb.append("NO").append("\n");
        }  
        System.out.println(sb.toString());
    }
    
}
