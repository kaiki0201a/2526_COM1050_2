import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.util.TreeSet;

import javax.imageio.IIOException;

public class SPOJ_MinStock {    
    static class Stock implements Comparable<Stock>{
        String name;
        int val;

        public Stock(String name, int val){
            this.name = name;
            this.val = val;
        }

        @Override
        public int compareTo(Stock other){
            if (this.val != other.val){
                return Integer.compare(this.val, other.val);
            }
            return this.name.compareTo(other.name);
        }
    }


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
    
        HashMap<String, Integer> map = new HashMap<>();
        TreeSet<Stock> set = new TreeSet<>();

        for (int i = 0; i < n; i ++){
            st = new StringTokenizer(br.readLine());

            String type = st.nextToken();
            if (type.equals("1")){

                String name = st.nextToken();
                int price = Integer.parseInt(st.nextToken());

                Stock s = new Stock(name, price);
                map.put(name, price);
                set.add(s);

            } else if (type.equals("2")){
                String name = st.nextToken();
                int newPrice = Integer.parseInt(st.nextToken());

                set.remove(new Stock(name, map.get(name)));

                map.put(name, newPrice);
                set.add(new Stock(name, newPrice));
            } else {
                String name = st.nextToken();

                Stock minSt = set.pollFirst();
                map.remove(minSt.name);

                sb.append(minSt.name).append(" ").append(i+1).append("\n");
            }
        }
        System.out.println(sb.toString()); 
    }
    
}
