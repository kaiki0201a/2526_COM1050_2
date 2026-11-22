import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};

public class LC_690_Employee_Importance {
    Map<Integer, Employee> map = new HashMap<>();
    public int getImportance(List<Employee> employees, int id) {
        for (Employee e: employees){
            map.put(e.id, e);
        }

        return dfs(id);
    }

    public int dfs(int id){
        Employee e = map.get(id);
        List<Integer> sub = e.subordinates;
        int total = e.importance;
        for (int i : sub){
            total += dfs(i);
        }
        return total;

    }
}
