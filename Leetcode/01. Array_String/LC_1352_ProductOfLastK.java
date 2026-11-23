import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LC_1352_ProductOfLastK {
    List<Integer> res;
    List<Integer> cum;
    Map<Integer, Boolean> map;

    public LC_1352_ProductOfLastK() {
        res = new ArrayList<>();
        cum = new ArrayList<>();
        cum.add(1);
        map = new HashMap<>();
    }

    public void add(int num) {
        res.add(num);
        if (num == 0){
            cum.add(1);
            map.put(cum.size(), true);
        } else {
            cum.add(cum.get(cum.size() - 1) * num );
        }
    }

    public int getProduct(int k) {
        for (Map.Entry<Integer, Boolean> e: map.entrySet()){
            if (e.getKey() > cum.size() - k)
                return 0;
        }
        System.out.println(cum.toString());
        return cum.get(cum.size() -1) / cum.get(cum.size() - 1 - k);
    }
}
