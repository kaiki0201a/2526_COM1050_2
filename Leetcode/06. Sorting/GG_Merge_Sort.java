public class GG_Merge_Sort {
    public static void merge(int[] a, int[] aux, int lo, int mid, int hi){
        // Sao chep a -> aux
        for (int i = lo; i <= hi; i ++){
            aux[i] = a[i];
        }

        // Merge
        int i = lo; int j = mid + 1;
        for ( int k = lo; k <= hi; k ++){
            if (i > mid) a[k] = aux[j++];
            else if (j > hi) a[k] = aux[i++];
            else if (aux[i] <= aux[j])   a[k] = aux[i++];
            else    a[k] = aux[j++];
        }
    }

    public static void mergeSort_1(int[] arr, int[] aux, int l, int r){
        if (l >= r) return;

        int mid = l + (r-l)/2;
        mergeSort_1(arr, aux, l, mid);
        mergeSort_1(arr, aux, mid+1, r);

        if (arr[mid] <= arr[mid+1]) return;

        merge(arr, aux, l, mid, r);
    }

    public static void mergeSort(int[] arr, int l, int r){
        int[] aux = new int[r - l + 1];
        mergeSort_1(arr, aux, l, r);
    }
}
