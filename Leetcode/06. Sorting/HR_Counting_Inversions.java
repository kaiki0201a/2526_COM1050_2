// https://www.hackerrank.com/challenges/ctci-merge-sort/problem

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HR_Counting_Inversions {
    public static long count = 0;   // long vi co the bi tran so

    public static void merge(int[] a, int[] aux, int lo, int mid, int hi){
        // Sao chep
        for (int i = lo; i <= hi; i++){
            aux[i] = a[i];
        }

        // Merge
        int i = lo; int j = mid + 1;
        for (int k = lo; k <= hi; k ++){
            if (i > mid)    a[k] = aux[j++];
            else if (j > hi)    a[k] = aux[i++];
            else if (aux[j] < aux[i]){
                a[k] = aux[j++];
                count += (mid - i + 1);
            } else a[k] = aux[i++];
        }
    }

    public static void mergeSort_1(int[] a, int[] aux, int lo, int hi){
        if (hi <= lo) return;

        int mid = lo + (hi-lo)/2;

        mergeSort_1(a, aux, lo, mid);
        mergeSort_1(a, aux, mid+1, hi);

        if (a[mid] <= a[mid+1]) return;

        merge(a, aux, lo, mid, hi);
    }

    public static void mergeSort(int[] a){
        int[] aux = new int[a.length];
        mergeSort_1(a, aux, 0, a.length-1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();

        int d = Integer.parseInt(st.nextToken());

        for (int i = 0; i < d; i ++){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            int[] arr = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j ++){
                arr[j] = Integer.parseInt(st.nextToken());
            }

            mergeSort(arr);

            sb.append(count).append("\n");
            count = 0;
        }
        System.out.println(sb.toString());
        }
    }

