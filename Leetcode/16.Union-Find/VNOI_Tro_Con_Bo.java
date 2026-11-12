import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class VNOI_Tro_Con_Bo {
    static int[] UF;
    static long[] sz; // Dùng kiểu long để lưu tổng số bò (tránh tràn số)

    // Hàm root duy nhất xử lý Nén đường + Cộng dồn bò
    public static int root(int p){
        if (p == UF[p]) return p;

        int oldParent = UF[p];

        UF[p] = root(UF[p]);

        if (UF[p] != oldParent)
            sz[p] += sz[oldParent];
        return UF[p];
    }

    public static void joinC(int x, int y){
        int i = root(x);
        int j = root(y);

        if (i == j) return;
        
        // Không dùng Union by Size để code đơn giản, 
        // cho j nhận i làm sếp
        UF[j] = i; 
        
        // Trừ đi số bò quá khứ của sếp i

        sz[j] -= sz[i];
    }

    public static void addC(int x, int v){
        int i = root(x);
        sz[i] += v;
    }

    public static long getSz(int x){
        int i = root(x);
        if (x == i) return sz[x]; // Nếu tự làm sếp thì chỉ lấy của chính mình
        return sz[x] + sz[i];     // Lấy của mình + của Sếp
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        UF = new int[n+1];
        sz = new long[n+1];
    

        for ( int i = 1; i < n+ 1; i++){
            UF[i] = i;
            sz[i] = 0;
  
        }

        for (int i = 0; i < k; i ++){
            st = new StringTokenizer(br.readLine());
            String type = st.nextToken();
            int x = Integer.parseInt(st.nextToken());

            if (type.equals("join")){
                int y = Integer.parseInt(st.nextToken());
                joinC(x, y);
                
            } else if (type.equals("add")) {
                int v = Integer.parseInt(st.nextToken());
                addC(x, v);
            }
            else{
                sb.append(getSz(x)).append("\n");
            }
        }

        System.out.print(sb.toString());
    }
}