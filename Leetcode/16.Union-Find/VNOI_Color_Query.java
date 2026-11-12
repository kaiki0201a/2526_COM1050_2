import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class VNOI_Color_Query {
    static int[] UF;
    static int[] sz;

    static Map<Integer, Integer>[] mapp;   // Mỗi root có một map

    public static int root(int i){
        if (i == UF[i]) return i;

        return UF[i] = root(UF[i]);
    }

    public static void union(int p, int q){
        int i = root(p);
        int j = root(q);

        if (i == j) return;

        if (sz[i] < sz[j]){
            int temp = i;
            i = j;
            j = temp;
        }

        UF[j] = i;
        sz[i] += sz[j];

        for (Map.Entry<Integer, Integer> entry : mapp[j].entrySet()){
            int m = entry.getKey();
            int count = entry.getValue();

            // Cong don
            mapp[i].put(m, mapp[i].getOrDefault(m, 0) + count);
        }
    }

    public static int getColor(int u, int v){
        return mapp[root(u)].getOrDefault(v, 0);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());   // Dinh
        int q = Integer.parseInt(st.nextToken());   // Truy van

        UF = new int[n+1];
        sz = new int[n+1];
        mapp = new HashMap[n+1];

        st = new StringTokenizer(br.readLine());


        // Init
        for (int i = 1; i < n + 1; i ++){
            UF[i] = i;
            sz[i] = 1;

            mapp[i] = new HashMap<>();
            int a = Integer.parseInt(st.nextToken());
            mapp[i].put(a, 1);
        }

        for (int i = 0; i < q; i ++){
            st = new StringTokenizer(br.readLine());

            int type = Integer.parseInt(st.nextToken());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            if (type == 1){
                union(u, v);
            } else if (type == 2){
                sb.append(getColor(u, v)).append("\n");
            }
        }

        System.out.println(sb.toString());
    }
}
