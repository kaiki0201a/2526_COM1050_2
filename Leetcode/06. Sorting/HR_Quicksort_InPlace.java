import java.util.Arrays;
import java.util.Scanner;

class HR_Quicksort_InPlace {

    public static int partition(int[] a, int lo, int hi){
        int pivot = a[hi];

        int i = lo;
        for (int j = i; j < hi; j ++){
            if (a[j] <= pivot){ // swap
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
                i += 1;
            }
        }
        a[hi] = a[i];
        a[i] = pivot;

        for (int x : a){
            System.out.print(x + " ");
        }
        System.out.println();

        return i;
    }

    public static void sort(int[] a, int lo, int hi){
        if (lo >= hi) return;

        int p = partition(a, lo, hi);
        sort(a, lo, p-1);
        sort(a, p + 1, hi);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        sc.nextLine();
        int[] arr = new int[a];

        for (int i = 0; i < a; i++){
            arr[i] = sc.nextInt();
        }

        sort(arr, 0, a-1);

        sc.close();
    }
}