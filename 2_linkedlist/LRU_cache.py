class DoubleNode:
    def __init__(self, key:int, val:int) -> None:
        self.val = val
        self.key = key
        self.next = None
        self.previous = None
        
        
        
class LRUCache:
    def __init__(self, cap) -> None:
        self.capacity = cap
        self.size = 0
        self.address = dict() # {key: DoubleNode ref}
        self.iter = None
        self.root = None
        
    def get(self, key:int):
        # return key's val or -1 if key's not existed
        if key not in self.address:
            return -1
        else:
            val = self.address[key].val
            self.put(key, val)
            return val
            
    
    def put(self, key: int, val: int):
        print(f"Current size = {self.size}, Current cap: {self.capacity}" )
        # update if exist, otherwise, add. If size > cap, evict the least recently used key
        new_node = DoubleNode(key, val)
        if self.size == 0:      # PUT 1st element into LRU
            self.iter = new_node
            self.root = new_node
            self.size = 1
            self.address[new_node.key] = new_node
            return
        if self.iter.key == key:  # If the key is the latest used element in LRU 
            self.iter.val = val
            return
        
        new_node.previous = self.iter
        self.iter.next = new_node
        self.iter = new_node
        
        if key in self.address: # key is existed
            past = self.address[key] # ref to the node which has the same key 
            past_pre, past_next = past.previous, past.next
            if past.previous : # past is not the 1st Node
                past_pre.next = past_next
                past_next.previous = past_pre
                del past
            else: # past is the 1st Node, size >= 2
                past_next.previous = None
                self.root = past_next
                del past
        else: # key not existed
            if self.size < self.capacity:  
                self.size += 1
                print('up size')
            else:  # size = capacity
                # delete the last node, update self.root, self.address[old_key], 
                print('del 1st Node')
                last_key = self.root.key
                self.root = self.root.next
                self.root.previous = None
                # if last.key:
                del self.address[last_key]
        # update ref of new node    
        self.address[key] = new_node
        
        
    def print(self):
        node = self.root
        output = ''
        while node:
            output += f"{node.key}: {node.val}, "
            node = node.next
        print(output)
            
                
                
# lRUCache = LRUCache(2)
# lRUCache.put(1, 1) # cache is {1=1}
# lRUCache.print()
# lRUCache.put(2, 2) # cache is {1=1, 2=2}
# lRUCache.print()
# print("1 ? ", lRUCache.get(1))   # return 1
# lRUCache.print()

# lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.print()
# print("-1 ?  ", lRUCache.get(2))   # returns -1 (not found)
# lRUCache.print()
# lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.print()
# print("-1 ?  ", lRUCache.get(1))    # return -1 (not found)
# lRUCache.print()
# print("3 ?  ", lRUCache.get(3))    # return 3
# lRUCache.print()
# print("4 ?  ", lRUCache.get(4))   # return 4
# lRUCache.print()

lRUCache = LRUCache(3)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.print()
lRUCache.put(2, 2) # cache is {1=1, 2=2}
lRUCache.print()
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.print()
lRUCache.put(4, 4) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.print()

print("4 ? ", lRUCache.get(4))   
print("3 ? ", lRUCache.get(3))   
print("2 ? ", lRUCache.get(2))   
print("-1 ? ", lRUCache.get(1))   

lRUCache.put(5, 5) # cache is {1=1, 2=2}
lRUCache.print()

print("-1 ? ", lRUCache.get(1))   
print("2 ? ", lRUCache.get(2))   
print("3 ? ", lRUCache.get(3))   
print("-1 ? ", lRUCache.get(4))   
print("5 ? ", lRUCache.get(5))   



              
            
                
                
                    
            
            
    