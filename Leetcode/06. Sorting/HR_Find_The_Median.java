import java.util.Scanner;

class HR_Find_The_Median {
    public static void swap(int[] a, int i, int j){
        int temp = a[i];
        a[i] = a[j]; a[j] = temp;
    }

    public static int partition(int[] a, int lo, int hi){
        int pivot = a[hi];
        int i = lo;

        for ( int j = i; j < hi; j++){
            if (a[j] <= pivot){
                swap(a, i, j);
                i += 1;
            }
        }
        swap(a, hi, i);

        return i;
    }

    public static int sort_select(int[] a, int lo, int hi){
        if (lo > hi) return -1;

        int p = partition(a, lo, hi);

        if (p == a.length/ 2){
            return a[p];
        } else if (p > a.length/2){
            return sort_select(a, lo, p -1);
        } else {
            return sort_select(a, p+1, hi);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        sc.nextLine();
        int[] arr = new int[a];

        for (int i = 0; i < a; i++){
            arr[i] = sc.nextInt();
        }
        System.out.println(sort_select(arr, 0, a-1));

        sc.close();
    }
    
}
