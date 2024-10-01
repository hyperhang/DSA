class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
       
        for i in range(0, len(arr)) :
            if (arr[i] == 0):
                for j in range(len(arr)-1, i, -1):
                    arr[j] = arr[j-1]
                i+=1 #// we don't want to traverse over the duplicate zero
            
        