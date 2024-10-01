# class MyCalendar:

#     def __init__(self):
#         self.root = []

#     def book(self, start: int, end: int) -> bool:
#         for cal in self.root:
#             if start >= cal[1] or end <= cal[0]:
#                 pass
#             else:
#                 return False
#         self.root.append([start, end])
#         return True


# 2nd solution: AVL Tree, BST


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10,20))
print(obj.book(15,25))
print(obj.book(20,30))