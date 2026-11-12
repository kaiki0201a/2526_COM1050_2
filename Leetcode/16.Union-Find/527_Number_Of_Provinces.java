class Solution {
    public int[] UF;
    public int[] sz;

    public int root(int i){
        while (i != UF[i])
            i = UF[i];
        return i;
    }

    public boolean connected(int q, int p){
        return root(p) == root(q);
    }

    public boolean union(int p, int q){     // union kiêm kiểm tra để count -= 1;
        int i = root(p);
        int j = root(q);
        if (i == j) return false;
        if (sz[i] > sz[j]){
            UF[j] = i;
            sz[i] += sz[j];
        } else {
            UF[i] = j;
            sz[j] += sz[i];
        }  
        return true;
    }

    public int findCircleNum(int[][] isConnected) {
        
        int N = isConnected.length;
        UF = new int[N];
        sz = new int[N];
        int count = N;
        // Init
        for (int i = 0; i < N; i++){
            UF[i] = i;
            sz[i] = 1;
        }

        for (int i = 0; i < N; i ++){
            for (int j = i + 1; j < N; j ++){
                if (isConnected[i][j] != 0){
                    if (union(i, j)) 
                    count -= 1;
                }

            }
        }
        return count;
        }
}
