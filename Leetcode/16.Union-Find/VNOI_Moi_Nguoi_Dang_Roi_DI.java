// Y tuong: tao them o trong de chua nhung nguoi da roi di;
// Khi người đã rời đi thì sẽ chuyển tiếp cho người bên cạnh khi cần hỏi đến
// Ví dụ 3 rời đi, UF[3] = 4; 2 rời đi, UF[2] = 3; khi ? 2 thực hiện root(2)->root(3) -> 4
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class VNOI_Moi_Nguoi_Dang_Roi_DI {
    static int[] UF;

    public static int root(int p){
        if (p == UF[p]) return p;

        return UF[p] = root(UF[p]);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        UF = new int[n+2];

        // Init
        for ( int i = 1; i < n + 2; i ++){
            UF[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            String type = st.nextToken();
            int u = Integer.parseInt(st.nextToken());

            if (type.equals("-")){
                UF[u] = root(u+1);
            } else if (root(u) > n){
                sb.append("-1\n");
            } else{
                sb.append(root(u)).append("\n");
            }
        
        }
        System.out.println(sb.toString());
    }
    
}
