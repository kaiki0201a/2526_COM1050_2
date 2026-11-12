import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


//         PriorityQueue<Integer> lowers = new PriorityQueue<>(Collections.reverseOrder()); // max heap
public class HR_Find_The_RunningMedian {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        PriorityQueue<Integer> pq1 = new PriorityQueue<>(); // max heap
        PriorityQueue<Integer> pq2 = new PriorityQueue<>(); // min heap


        StringBuffer sb = new StringBuffer();

        int n = Integer.parseInt(st.nextToken());
        int count = 0;

        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());

            int t = Integer.parseInt(st.nextToken());
            int value = count % 2;
            if (value == 0){
                pq1.offer(-t);
            } else {
                pq2.offer(t);
            }
            
            while (count >= 1 && -pq1.peek() > pq2.peek()){
                int newMax = pq2.poll();
                int newMin = -pq1.poll();

                pq1.offer(-newMax);
                pq2.offer(newMin);
            }

            count += 1;
            if (value == 0){
                sb.append(String.format("%.1f", (double) -pq1.peek())).append("\n");
            } else {
                double median = ((double) -pq1.peek() + (double) pq2.peek()) / 2.0;
                sb.append(String.format("%.1f", median)).append("\n");
            }
        }
        System.out.println(sb.toString());
    }
    
}
