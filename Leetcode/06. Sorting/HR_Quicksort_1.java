import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class HR_Quicksort_1 {

    public static List<Integer> quickSort(List<Integer> arr) {
    // Write your code here
        List<Integer> leftList = new ArrayList<>();
        List<Integer> equalsList = new ArrayList<>();
        List<Integer> rightList = new ArrayList<>();

        int pivot = arr.get(0); 

        for (int i : arr){
            if (i < pivot) leftList.add(i);
            else if (i == pivot) equalsList.add(i);
            else rightList.add(i);
        }
        leftList.addAll(equalsList);
        leftList.addAll(rightList);
        
        return leftList;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        List<Integer> arr = new ArrayList<>();
        sc.nextLine();

        for (int i = 0; i < a; i ++){
            arr.add(sc.nextInt());
        }

        System.out.println(quickSort(arr));

        
    }

}
