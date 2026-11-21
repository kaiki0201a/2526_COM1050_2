import java.util.List;

class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
public class LC_559_MaxDepthOfNaryTree {
    public int maxDepth(Node root) {
        if (root == null)
            return 0;
        int depth = 0;
        for (Node no: root.children){
            depth = Math.max(depth, maxDepth(no));
        }
        return depth + 1;
    }
}
