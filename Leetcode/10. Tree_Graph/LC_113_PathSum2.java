import java.util.ArrayList;
import java.util.List;

class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
 }

public class LC_113_PathSum2 {
    List<List<Integer>> res = new ArrayList<>();

    List<Integer> subRes = new ArrayList<>();

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        dfs(root, targetSum, 0);

        return res;
    }
    public void dfs(TreeNode root, int targetSum, int cur){
        if (root == null)
            return;
        subRes.add(root.val);

        if (cur + root.val == targetSum && root.left == null && root.right == null){
            res.add(new ArrayList<>(subRes));
        } else {
            dfs(root.left, targetSum, cur + root.val);
            dfs(root.right, targetSum, cur + root.val);
        }

        subRes.remove(subRes.size() - 1);
    }
}
