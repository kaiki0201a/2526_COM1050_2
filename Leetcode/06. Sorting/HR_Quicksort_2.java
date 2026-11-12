import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class HR_Quicksort_2 {
    public static List<Integer> sort(List<Integer> arr){

        if (arr.size() < 2) return arr;

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
        
        // Thuc hien de quy
        List<Integer> left = sort(leftList);
        List<Integer> right = sort(rightList);

        List<Integer> res = new ArrayList<>();
        res.addAll(left);
        res.addAll(equalsList);
        res.addAll(right);

        for (int x : res){
            System.out.print(x + " ");
        }
        System.out.println();
        return res;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();

        List<Integer> arr = new ArrayList<>();
        for (int i =0; i < a; i ++){
            arr.add(sc.nextInt());
        }

        sort(arr);
    }
}
