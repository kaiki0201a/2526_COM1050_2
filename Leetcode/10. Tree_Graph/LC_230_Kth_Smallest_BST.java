import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }

class Solution {
    public static void inoder(TreeNode root, List<Integer> list){
        if (root == null) return;
        inoder(root.left, list);
        list.add(root.val);
        inoder(root.right, list);
    }

    public int kthSmallest(TreeNode root, int k) {
        List<Integer> list = new ArrayList<>();

        inoder(root, list);
        
        return list.get(k-1);
    }
}
 */