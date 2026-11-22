public class LC_2124_CheckABeforeB {
    public boolean checkString(String s) {
        boolean check = false;

        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == 'b')
                check = true;
            else{
                if (check)
                    return false;
            }
        }

        return true;
    }
}
