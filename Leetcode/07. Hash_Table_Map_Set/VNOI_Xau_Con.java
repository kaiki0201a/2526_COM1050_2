import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class VNOI_Xau_Con {
    // Dinh nghia hang so
    static final int BASE = 311;
    static final long MOD = 1000000007L; //Chữ L ép kiểu sang 64-bit Long

    // Khai bao mang toan cuc
    static long[] POW;
    static long[] hashT;

    // Hàm trích xuất mã Hash của chuỗi con từ vị trí i đến j
    static long getHashT(int i, int j) {
        // Cong thuc
        long hashValue = (hashT[j] - hashT[i-1]* POW[j-i+1] + MOD*MOD) % MOD;
        return hashValue;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String T = br.readLine();
        String P = br.readLine();

        if (T == null ||  P == null) return;

        int lenT = T.length();
        int lenP = P.length();

        // Them khoang trang de index bat dau tu 1
        T = " " + T;
        P = " " + P;

        POW = new long[lenT + 1];
        hashT = new long[lenT + 1];

        // 1. Tinh truoc mang luy thua cua Base
        POW[0] = 1;
        for (int i = 1; i <= lenT; i++){
            POW[i] = (POW[i-1]*BASE) % MOD;
        }

        // 2. Tinh mang Prefix Hash cho chuoi T
        hashT[0] = 0;
        for (int i = 1; i <= lenT; i++){
            hashT[i] = (hashT[i-1]*BASE + T.charAt(i)) % MOD;
        }

        // 3. Tinh hashP
        long hashP = 0;
        for (int i = 1; i<= lenP; i++){
            hashP = (hashP * BASE + P.charAt(i)) % MOD;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= lenT - lenP + 1; i ++){
            if (hashP == getHashT(i, i + lenP - 1)){
                sb.append(i).append(" ");
            }
        }

        System.out.println(sb.toString());
    }
}
