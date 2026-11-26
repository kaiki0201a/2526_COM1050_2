public class LC_3360_StoneRemovalGame {
    public boolean canAliceWin(int n) {
        boolean alice = false;
        int i = 10;

        while (n > 0){
            if (n - i >= 0){
                n -= i;
                alice = !alice;
            } else{
                break;
            }
            i--;
        }

        return alice;
    }
}
