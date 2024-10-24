class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # abcd: 3,4,5,3.  n=2
        # cbacdbc.   abcd: 2,2,2,2
        # 