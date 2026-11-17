public class LC_1524_NumberOfSubArraysWithOdd {
    public int numOfSubarrays(int[] arr) {
        int prefixSum = 0;
        int countL = 0;
        int res = 0;
        int countR = 0;

        for (int i = 0; i < arr.length; i++){
            prefixSum += arr[i];

            if (arr[i] % 2 == 0){
                res += countL;
            } else {
                res += countR + 1;
            }

            if (prefixSum % 2 != 0)
                countL++;
            else
                countR++;

            if (arr[i] % 2 == 0){
                countR++;
            } else {
                countL++;
            }
        }

        return res;
    }
}
