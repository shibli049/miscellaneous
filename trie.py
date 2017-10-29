class Node:
    def __init__(self, count = 1):
        self.next = {}
        self.end = False
        self.count = count


class Trie:
    def __init__(self):
        self.root = Node(count = 0)

    def add(self, prefix):
        curr = self.root
        for i in range(len(prefix)):
            id = prefix[i]
            if(id not in curr.next):
                curr.next[id] = Node()
            else:
                curr.next[id].count += 1
            curr = curr.next[id]
        curr.end = True

    def find(self, prefix):
        curr = self.root
        for i in range(len(prefix)):
            id = prefix[i]
            if(id not in curr.next):
                return False,0
            curr = curr.next[id]
        return curr.end,curr.count