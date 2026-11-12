import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class VNOI_Gia_Tri_Tap {
    static int[] UF;
    static int[] sz;
    static int[] minNode;
    static int[] maxNode;

    public static int root(int i){
        if (i == UF[i]) return i;

        return UF[i] = root(UF[i]);
    }

    public static void union(int u, int v){
        int i = root(u);
        int j = root(v);
        if (i == j) return;

        int minNode1 = (minNode[i] < minNode[j]) ? minNode[i] : minNode[j];
        int maxNode1 = (maxNode[i] > maxNode[j]) ? maxNode[i] : maxNode[j];

        if (sz[i] > sz[j]){
            UF[j] = i;
            sz[i] += sz[j];
            minNode[i] = minNode1;
            maxNode[i] = maxNode1;
        } else {
            UF[i] = j;
            sz[j] += sz[i];
            minNode[j] = minNode1;
            maxNode[j] = maxNode1;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());   // Dinh
        int m = Integer.parseInt(st.nextToken());   // Truy van

        UF = new int[n+1];
        sz = new int[n+1];
        minNode = new int[n+1];
        maxNode = new int[n+1];

        for (int i = 1; i < n+1 ;i++){
            UF[i] = i;
            sz[i] = 1;
            minNode[i] = i;
            maxNode[i] = i;
        }

        for (int i = 0; i < m; i ++){
            st = new StringTokenizer(br.readLine());

            String type = st.nextToken();
            int u = Integer.parseInt(st.nextToken());

            if (type.equals("union")){
                int v = Integer.parseInt(st.nextToken());
                union(u, v);
            } else {
                int j = root(u);
                sb.append(minNode[j]).append(" ")
                  .append(maxNode[j]).append(" ")
                  .append(sz[j]).append("\n");
            }
        }
        System.out.println(sb.toString());
    }
}
