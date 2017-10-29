public class Trie{
    Node root = new Node(0);

    public void add(String prefix){
        Node curr = this.root;
        for( Character id : prefix.toCharArray()){
            if(curr.next.containsKey(id)){
                curr.next.get(id).count += 1;
            }else{
                curr.next.put(id, new Node());
            }
            curr = curr.next.get(id);
        }
    }

    public int findPossibleCount(String prefix){
        Node curr = this.root;
        for( Character id : prefix.toCharArray()){
            if(!curr.next.containsKey(id)){
                return 0;
            }
            curr = curr.next.get(id);
        }
        return curr.count;
    }

    public int find(String prefix){
        Node curr = this.root;
        for( Character id : prefix.toCharArray()){
            if(!curr.next.containsKey(id)){
                return False;
            }
            curr = curr.next.get(id);
        }
        return curr.end;
    }

}

class Node{
    HashMap<Character, Node> next = new HashMap<>();
    boolean end = false;
    int count = 1;
    public Node(){
    }

    public Node(int count){
        this.count = count;
    }
}