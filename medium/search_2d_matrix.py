import bisect
class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        top_ind = bisect.bisect(matrix[0], target)
        first_column = []
        for c in range(len(rows)):
            first_column.append(matrix[c][0])
        print("first col:", first_column)
        left_ind = bisect.bisect(first_column, target)
        while top_ind>=0 and left_ind>=0 :
            if target <= matrix[top_ind][left_ind] and target >= matrix[top_ind-1][left_ind-1]:
                # in this case, the target can only at vertical dir from top_ind to left_ind(Ox)
                #                                or at horizontal dir from left_ind to top_ind(Oy)
                if target == matrix[top_ind][left_ind] or target == matrix[top_ind-1][left_ind-1]:
                    return True
                
                for i_vertical in range(left_ind):
                    if matrix[i_vertical][top_ind] == target:
                        return True
                for i_horizontal in range(top_ind):
                    if matrix[left_ind][i_horizontal] == target:
                        return True
                return False
            else:
                
        
# 0 2    4     6    8
# 1 1000 1001 1002  1003
# 2 1001 1002 1003  1004
# 4 1002 1003 1004  1005