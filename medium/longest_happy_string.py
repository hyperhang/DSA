from sortedcontainers import SortedDict
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        a,b,c: 53,36,77
        a,b,c: 17, 0,41:  aabbccaabbcc....aabbcc
        a,b,c: 1 ,  ,25:   ...aabbcc...ccbbccbb...ccbbccbcc
        
        a,b,c: 15, 18, 36
        
        (acc)*9, abc: 6, 18,18
        (acc)*9 (bc)*12, abc: 6,6,6
        (acc)*9 (bc)*12 (abc)*6
        
        a,b,c: 6, 18, 36
        (acc)*6, bc: 18, 24
        (bcc)*6 , bc: 12,12
        (bc)*12
        ccbccbccb..., abc: 6,6,12
        ccbccaccbcca...
        
        abc : 12,12,16
        (bcc)*2, abc: 12, 10, 12
        ccbccb, abc: 12, 10, 12
        ccbccbcacacbacba...
        
        """

        hq = []
        if a > 0:
            heapq.heappush(hq, [-a, 'a'])
        if b > 0:
            heapq.heappush(hq, [-b, 'b'])
        if c > 0:
            heapq.heappush(hq, [-c, 'c'])
        ans = ''
        while len(hq) :
            max_key = heapq.heappop(hq)
            char = max_key[1]
            if len(ans) < 2 or (ans[-1] == char and ans[-2] != char) or ans[-1] != char:
                ans += char
                if max_key[0]+1 !=0 :
                    heapq.heappush(hq, [max_key[0]+1, char])
            else:
                if len(hq):
                    second_max_key = heapq.heappop(hq)
                    char = second_max_key[1]
                    ans += char
                    if second_max_key[0]+1 != 0:
                        heapq.heappush(hq, [second_max_key[0]+1, char])
                    heapq.heappush(hq, max_key)
        return ans
        # TC: O(a+b+c)
        # SC: O(a+b+c)
    
sol = Solution()
a = 1
b = 1
c = 7

a = 7
b = 1
c = 0
print(sol.longestDiverseString(a,b,c))

            
                
            
        
        
        
        
        
        
        
        
             
        