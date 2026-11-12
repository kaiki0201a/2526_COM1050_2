// Y tuong, tim o gan nhat ben phai chua bi chiem

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class VNOI_Parking {
    static int[] UF;

    public static int findEmpty(int i){

        int n = UF.length - 1;
        if (i == UF[i]){
            UF[i] = (i % n) + 1;
            return i;
        }

        return UF[i] = findEmpty(UF[i]);
    }
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());   // Numbers of cars

        UF = new int[n+1];
        
        // Init
        for ( int i = 1; i < n+1; i++){
            UF[i] = i;
        }

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i ++ ){
            int a = Integer.parseInt(st.nextToken());
            int p = findEmpty(a);
            sb.append(p).append(" ");
            
        }
        System.out.println(sb.toString());
    }
}
