class LC_706_Design_HashMap {
    private class Node {
        int key;
        int value;
        Node next;

        public Node(int key, int value){
            this.key = key;
            this.value = value;
            this.next = null;
        }
    }

    private final int SIZE = 10007;
    private Node[] buckets;

    private int hash(int key) {
        return key % SIZE;
    }

    public MyHashMap() {
        buckets = new Node[SIZE];
    }
    
    public void put(int key, int value) {
        int index = hash(key);
        Node head = buckets[index];

        Node curr = head;
        while (curr != null){
            if (curr.key == key) {
                curr.value = value;
                return;
            }
            curr = curr.next;
        }

        Node newNode = new Node(key, value);
        newNode.next = head;
        buckets[index] = newNode;
    }
    
    public int get(int key) {
        int index = hash(key);
        Node curr = buckets[index];

        while (curr != null){
            if (curr.key == key){
                return curr.value;
            }
            curr = curr.next;
        }

        return -1;
    }
    
    public void remove(int key) {
        int index = hash(key);
        Node curr = buckets[index];

        if (curr == null) return;

        if (curr.key == key) {
            buckets[index] = curr.next;
            return;
        }

        while (curr.next != null){
            if (curr.next.key == key){
                curr.next = curr.next.next;
                return;
            }
            curr = curr.next;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */