class ListNode: 
        def __init__(self, key,next = None): 
            self.key = key 
            self.next = next

class MyHashSet:


    def __init__(self):
        self.set = [ListNode(0) for i in range(10000)]
        
        

    def add(self, key: int) -> None:
        bucket = key % len(self.set)
        curr = self.set[bucket]

        while curr.next: 
            if curr.next.key == key: 
                return 
            curr = curr.next 
        curr.next = ListNode(key)
        
        

    def remove(self, key: int) -> None:
        bucket = key % len(self.set)
        curr = self.set[bucket]

        while curr.next: 
            if curr.next.key == key: 
                curr.next = curr.next.next 
                return 
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        bucket = key % len(self.set)
        curr = self.set[bucket]

        while curr.next: 
            if curr.next.key == key: 
                return True 
            curr = curr.next 
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)