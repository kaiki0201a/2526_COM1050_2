import java.util.*;

public class Main {

    static int[] id;
    static int[] sz;
    
    public static int root(int p)
    {
        while (p != id[p])
            p = id[p];
        return p;
    }

    // get u v
    public static boolean get(int u, int v){
        return root(u) == root(v);
    }

    public static void union(int u, int v){
        int i = root(u);
        int j = root(v);
        if ( i == j) return;
        
        if (sz[i] > sz[j]){
            id[j] = i;
            sz[i] += sz[j];
        } else{
            id[i] = j;
            sz[j] += sz[i];
        }
    }
    

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();   // So phan tu
        int m = sc.nextInt();   // So truy van
        sc.nextLine();
        id = new int[n+1];
        sz = new int[n+1];

        // Init
        for (int i = 0; i < n+1; i ++){
            id[i] = i;
            sz[i] = 1;
        }

        for ( int i = 0; i < m; i ++){
            String s = sc.nextLine();
            String[] str = s.split(" ");
            int u = Integer.parseInt(str[1]);
            int v = Integer.parseInt(str[2]);
            
            if (str[0].equals("union")){
                union(u, v);
            } else if (get(u,v) == true){
                System.out.println("YES");
            } else
                System.out.println("NO");
        }
    }
}