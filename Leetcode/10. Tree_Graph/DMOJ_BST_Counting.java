import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class DMOJ_BST_Counting {

    static Node N;
    static int count = 0;

    static class Node{
        int val;
        Node left, right;

        Node(int val){ this.val = val; }
        Node(int val, Node left, Node right){
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    static Node insert(int x, Node N){
        if (N == null) {
            System.out.println(count);
            return new Node(x);
        }
        count += 1;

        if (x < N.val){
            N.left = insert(x, N.left);
        } else {
            N.right = insert(x, N.right);
        }
        return N;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            int val = Integer.parseInt(st.nextToken());

            N = insert(val, N);
        }
    }
}
