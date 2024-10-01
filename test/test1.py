#                    1 : (0)
#             0 (1)                 1(2)
#       0(3)        1 (4)       0 (5)    1(6)

#     1(7)  0(8)   1(9) 1(10)     n  n   n  n

# travelling:
# O(h) , O(h)

class Solution():
    
    sum = 0
    def sum_of_tree_paths(self, ar: list):
        def check_path(i, path_sum=0):
            # print("i: ", i)
            current_sum = path_sum*2 + ar[i]
            
            if i*2+1 < len(ar):
                # has left child node
                print("left: ", current_sum)
                check_path(i*2+1, current_sum)
            if i*2+2 < len(ar):
                # has right child node
                print("right: ", current_sum)
                check_path(i*2+2, current_sum)
            if i*2+1 >= len(ar) and i*2+2 >= len(ar):
                # leaf:
                self.sum = self.sum + current_sum
                print("---leaf: ", self.sum)
                # print("sum : ", self.sum)
                return
        check_path(0,0)
        print(self.sum)
        return sum
    
s = Solution()
# 1 0 0
s.sum_of_tree_paths([1,0,1,0,1,0,1])  
#      1
#  0       1
# 0  1   0    1
# 100, 101, 110, 111
# 2^2*1 + 2^1*0 + 2^2*0

# 4, 5, 6, 7
# 22


# s.sum_of_tree_paths([1,0,1])
# #   1
# # 0   1
# 10, 11
# 1, 3

# s.sum_of_tree_paths([1,0,0])
# #   1
# # 0   0
# 10
# 1