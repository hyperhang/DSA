class Solution:
    def reverse_array(self, arr: list) -> list:
        res = []
        for i in range(len(arr)-1, -1,-1):
            res.append(arr[i])
        return res
    
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        rows = len(mat)
        cols = len(mat[0])
        i, j = 0, 0
        count = 0
        result = []
        while i <= rows -1 and j <= cols - 1:
            temp = [mat[i][j]]
            print("start: ", temp)
            _i = i
            _j = j
            while _i < rows - 1 and _j > 0:
                _i += 1
                _j -= 1
                temp.append(mat[_i][_j])            
            true_diagonal = self.reverse_array(temp) if count%2==0 else temp    
            result += true_diagonal    
            print("res: ", result)
            count += 1
            j += 1
            print("i, j: ", i, ", ", j)
            if j == cols :
                if i < rows - 1:
                    j = cols - 1
                    i += 1
                    continue
                if i == rows - 1:
                    break
        print(result)            

        return result    
                
s = Solution()
# mat = [[1,2,3],[4,5,6],[7,8,9]]
# mat = [[1,2],[3,4]]
mat = [ [1], [2], [3] ]
mat = [ [1,2,3] ]
mat = [ [1,2]]
s.findDiagonalOrder(mat)
               
