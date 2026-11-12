import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class HR_Jesse_And_Cookies {
    public static void sink(int[] a, int k, int N){
        while (2*k <= N){
            int j = 2*k;
            if (j < N){
                if (a[j] > a[j+1]){
                    j += 1;
                }
            }
            if (a[k] <= a[j]) break;

            exch(a, k, j);
            k = j;
        }
    }
    public static void swim(int[] a, int k, int n){
        while (k > 1){
            if (a[k/2] > a[k]){
                exch(a, k, k/2);
                k /=2;
            }
            else break;
        }
    }
    public static void insert(int[] a, int k, int n){
        a[++n] = k;
        swim(a, n, n);
    }

    public static void exch(int[] a, int i, int j){
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    public static boolean isEmpty(int[] a, int N){
        return N == 0;
    }

    public static int getMin(int[] a, int N){
        int res = a[1];
        exch(a, 1, N--);
        sink(a, 1, N);
        return res;
    }


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] minHeap = new int[n+1];
        
        for (int i = 1; i <= n; i ++){
            minHeap[i] = Integer.parseInt(st.nextToken());
        }

        // Tao min Heap
        for (int p = n/2; p >= 1; p--){
            sink(minHeap, p, n);
        }

        int count = 0;
        while (!isEmpty(minHeap, n)) {
            int st1 = getMin(minHeap, n);
            n -= 1;
            if (st1 >= k) {
                System.out.println(count);
                break;
            }
            int st2;
            if (!isEmpty(minHeap, n)) {
                st2 = getMin(minHeap, n);
            } else {
                System.out.println(-1);
                break;
            }
            n -= 1;
            int newval = (st1 + 2*st2);
            insert(minHeap, newval, n);
            n += 1;
            count += 1;
        }
    }
    
}
/*
    public static void main(String[] args) throws IOException {       
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++){
            pq.offer(Integer.parseInt(st.nextToken()));
        }
        int count = 0;
        while (!pq.isEmpty() && pq.peek() < k) {
            if (pq.size() < 2) {
                System.out.println(-1);
                break;
            }

            int c1 = pq.poll();
            int c2 = pq.poll();
            pq.offer(c1 + c2*2);

            count +=1;
        }

        if (pq.peek() >= k)
            System.out.println(count);

    }

}
    */