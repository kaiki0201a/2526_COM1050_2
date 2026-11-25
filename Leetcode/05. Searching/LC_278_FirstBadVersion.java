
public class LC_278_FirstBadVersion {
    boolean isBadVersion(int i){
        return true;
    }
    public int firstBadVersion(int n) {
        return search(0, n);
    }
    public int search(int lo, int hi){
        int mid = lo + (hi-lo)/2;

        if (lo > hi)
            return - 1;

        if (isBadVersion(mid)){
            int ne = search(lo, mid -1);
            return (ne != -1) ? ne : mid;
        }
        else
            return search(mid + 1, hi);
    }
}
