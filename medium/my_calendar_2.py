# class MyCalendarTwo:

#     def __init__(self):
#         self.root = []

#     def book(self, start: int, end: int) -> bool:
#         print(f"\n\ncurrent root: {self.root}\--> {start}, {end}")
#         overlap = []
#         for book in self.root:
#             if end <= book[0] or start >= book[1]:
#                 pass
#             else:
#                 overlap.append([max(start, book[0]), min(end, book[1])])
#         # check overlap contains any overlap again
#         overlap.sort()
#         print("Overlap:", overlap)
#         for i in range(1, len(overlap)):
#             if overlap[i][0] < overlap[i-1][1]:
#                 return False
        
#         # if not:
#         self.root.append([start,end])
#         return True

from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.root = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.root[start] = self.root.get(start, 0) + 1  # TC: O(log N)
        self.root[end] = self.root.get(end, 0) - 1
        
        su = 0
        for v in self.root.values(): # O(N)
            su += v
            if su == 3:
                self.root[start] -= 1 # O(log N)
                self.root[end] += 1
                if self.root[start] == 0:
                    del self.root[start]
                if self.root[end] == 0:
                    del self.root[end]
                return False
            
        return True
        # TC of book function: O(N), because we just iterate over a sorted tree by pre-order traversal.
        


# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
print(obj.book(10, 20))
print(obj.book(50, 60))
print(obj.book(10, 40))
print(obj.book(5, 15))
print(obj.book(5, 10))
print(obj.book(25, 55))