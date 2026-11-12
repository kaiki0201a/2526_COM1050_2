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

public class LC_450_DeleteNode_InBST{
    private static TreeNode deleteMin(TreeNode x){
        if (x.left == null) return x.right;
        x.left = deleteMin(x.left);
        return x;
    }

    public static TreeNode minNode(TreeNode root){
        while (root.left != null){
            root = root.left;
        }
        return root;
    }

    public static TreeNode delete(TreeNode root, int key){

        if (root == null) return null;
        if (key > root.val) root.right = delete(root.right, key);
        else if (key < root.val) root.left = delete(root.left, key);

        else{
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;

            TreeNode t = root;
            root = minNode(t.right);
            root.right = deleteMin(t.right);
            root.left = t.left;
        }
        return root;
    }

    public TreeNode deleteNode(TreeNode root, int key) {
        root = delete(root, key);
        return root;
    }
}
 */