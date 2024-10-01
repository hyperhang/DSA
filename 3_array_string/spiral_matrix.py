class Solution:
    result = []
    def bounding_array(self, matrix, i, j, m, n):
        # print(f"i: {i} , j: {j} , m: {m} , n: {n}")
        if m > i and n>j:
            for _j in range(j, n+1):    # hang dau tien
                self.result.append(matrix[i][_j])
            if m-i >= 2:                # vien ben phai cung
                for _i in range(i+1, m):
                    self.result.append(matrix[_i][n])
            else:
                pass # ko co vien ben phai cung
            for _j in range(n, j-1, -1): # hang cuoi cung
                self.result.append(matrix[m][_j])
            if m-i >= 2:                # vien ben trai cung
                for _i in range(m-1, i, -1):
                    self.result.append(matrix[_i][j])
            else:
                pass # ko co vien ben trai cung
            self.bounding_array(matrix, i+1, j+1, m-1, n-1)
        elif m == i and n == j:
            self.result.append(matrix[i][j])
            return -1
        elif m == i:
            for _j in range(j, n+1):
                self.result.append(matrix[i][_j])
            return -1
        elif n == j:
            for _i in range(i, m+1):
                self.result.append(matrix[_i][j])
            return -1
        else:
            return -1    
        
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        i, j, m, n = 0, 0, len(matrix)-1, len(matrix[0])-1
        self.bounding_array(matrix, i, j, m, n)
        res = self.result
        print(res)
        return res

s = Solution()
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[1]]
matrix = [[1,2]]
matrix = [[1],[2],[3]]
matrix = [[1,2,3],[4,5,6]]
matrix = [ [1,2], [3,4], [5,6] ]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))