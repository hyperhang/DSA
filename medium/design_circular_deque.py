class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.root = []

    def insertFront(self, value: int) -> bool:
        if len(self.root) < self.size:
            self.root.insert(0, value)
            print(f"root: {self.root}, size: {self.size}")
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.root) < self.size:
            self.root.append(value)
            print(f"root: {self.root}, size: {self.size}") 
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.root) > 0:
            del self.root[0]
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.root) > 0:
            del self.root[-1]
            return True
        return False

    def getFront(self) -> int:
        if len(self.root) > 0:
            return self.root[0]
        return -1

    def getRear(self) -> int:
        if len(self.root) > 0:
            return self.root[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.root) == 0

    def isFull(self) -> bool:
        return self.size == len(self.root)
        


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
param_1 = obj.insertLast(1)
print(param_1)
param_2 = obj.insertLast(2)
print(param_2)
param_3 = obj.insertFront(3)
print(param_3)
param_4 = obj.insertFront(4)
print(param_4)
param_5 = obj.getRear()
print(param_5)
param_6 = obj.isFull()
print(param_6)
param_7 = obj.deleteLast()
print(param_7)
param_8 = obj.insertFront(4)
print(param_8)
param_8 = obj.getFront()
print(param_8)

size = 3
1,2
3,1,2
insertFront: 4 - False
getRear: 2