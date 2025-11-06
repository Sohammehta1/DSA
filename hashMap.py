class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.next: Node = None

class MyHashMap:

    __SIZE = 100000
    def __init__(self):
        self.nodes = [None]*MyHashMap.__SIZE # array of nodes

    @staticmethod
    def getIndex(key):
        return hash(key)%MyHashMap.__SIZE
    
    def getPrev(self, key, node):
        prev = None
        head = node

        while(head is not None and head.key != key):
            prev = head
            head = head.next
        return prev

    def put(self, key: int, value: int) -> None:
        index: int = MyHashMap.getIndex(key)
        if(self.nodes[index]==None):
            self.nodes[index]=Node(-1,-1)
        prev = self.getPrev(key,self.nodes[index])

        if prev.key != key:
            newNode= Node(key,value)
            prev.next, newNode.next = newNode, prev.next

    def get(self, key: int) -> int:
        index: int = MyHashMap.getIndex(key)
        val = -1
        if self.nodes[index] is not None:
            prev: Node = self.getPrev(key,self.nodes[index])
            if prev.key != -1:
                val = prev.value
        return val

    def remove(self, key: int) -> None:
        index: int = MyHashMap.getIndex(key)
        if self.nodes[index] is not None:
            prev = self.getPrev(key,self.nodes[index])
            if prev.next is not None:
                prev.next = prev.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)