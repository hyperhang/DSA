from collections import defaultdict
from sortedcontainers import SortedDict
class AllOne:

    def __init__(self):
        self.root = defaultdict(int)
        self.sd = SortedDict() # 4: set("hello", "hi",..) , 3: set("ada", "ok"), ...
        
    def inc(self, key: str) -> None:
        self.root[key] = self.root.get(key, 0) + 1
        if self.root[key] == 1:
            if 1 in self.sd:
                self.sd[1].add(key)
            else:
                self.sd[1] = set([key])
        else:
            self.sd[self.root[key]-1].remove(key)
            if len(self.sd[self.root[key]-1]) == 0:
                del self.sd[self.root[key]-1]
            if self.root[key] in self.sd:
                self.sd[self.root[key]].add(key)
            else:
                self.sd[self.root[key]] = set([key])
        
    def dec(self, key: str) -> None:
        self.root[key] -= 1
        if self.root[key] == 0:
            self.sd[1].remove(key)
            del self.root[key]
            if len(self.sd[1]) == 0:
                del self.sd[1]
        else:
            self.sd[self.root[key]+1].remove(key)
            if len(self.sd[self.root[key]+1]) == 0:
                del self.sd[self.root[key]+1]
            if self.root[key] in self.sd:
                self.sd[self.root[key]].add(key)
            else:
                self.sd[self.root[key]] = set([key])
                
    def getMaxKey(self) -> str:
        if len(self.sd) == 0 :
            return ""
        return next(iter(self.sd.peekitem(-1)[1]))

    def getMinKey(self) -> str:
        if len(self.sd) == 0 :
            return ""
        return next(iter(self.sd.peekitem(0)[1]))
        

# Your AllOne object will be instantiated and called as such:
allOne = AllOne()
allOne.inc("hello")
allOne.inc("hello")
print(allOne.getMaxKey())
print(allOne.getMinKey())
allOne.inc("leet")
print(allOne.getMaxKey())
print(allOne.getMinKey() )
allOne.inc("hello")
allOne.inc("hello")
allOne.inc("leet")
print(allOne.getMaxKey())
print(allOne.getMinKey() )
allOne.inc("ada")
print(allOne.getMaxKey())
print(allOne.getMinKey() )
