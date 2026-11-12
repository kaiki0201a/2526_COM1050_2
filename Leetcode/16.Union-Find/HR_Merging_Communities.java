import java.io.*;
import java.util.StringTokenizer;


public class HR_Merging_Communities {
    
    static int[] UF;
    static int[] sz;

    // Hàm tìm gốc kết hợp nén đường (Path Compression)
    public static int root(int i){
        if (i == UF[i]) return i;

        return UF[i] = root(UF[i]);
    }

    // Hàm gộp
    public static void union(int i, int j){
        int rootI = root(i);
        int rootJ = root(j);

        if (rootI == rootJ) return;

        if (sz[rootI] < sz[rootJ]) {
            UF[rootI] = rootJ;
            sz[rootJ] += sz[rootI];
        } else {
            UF[rootJ] = rootI;
            sz[rootI] += sz[rootJ];            
        }
    }
    
    public static void main(String[] args) throws IOException {
        // Khởi tạo Fast I/O
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        java.util.StringTokenizer st = new java.util.StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // Số lượng người dùng
        int q = Integer.parseInt(st.nextToken()); // Queries

        UF = new int[n + 1];
        sz = new int[n + 1];

        // Init
        for (int i = 0; i< n + 1; i ++) {
            UF[i] = i;
            sz[i] = 1;
    
        }

        // Dùng StringBuilder để gom kết quả
        StringBuilder sb = new StringBuilder();
    
        for (int i = 0; i < q; i ++) {
            st = new StringTokenizer(br.readLine());
            String type = st.nextToken();

            if (type.equals("M")) { // Merge
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                union(u, v);
            } else if (type.equals("Q")) { // Query
                int u = Integer.parseInt(st.nextToken());

                int rootU = root(u);

                sb.append(sz[rootU]).append("\n");
            }
        }

        //
        System.out.println(sb.toString());

    }

}
