import copy
class Solution(object):
    """docstring for Solution."""
    def find_comb(self, ar: list):
        bin_list = []
        combs = []
        n = len(ar)
        def gen_next(length: int, current_list: list):
            if length + 1 <= n:
                for i in range(2):
                    _temp = copy.deepcopy(current_list)
                    _temp.append(i)
                    gen_next(length+1, _temp)
            else:
                bin_list.append(current_list)
                return
        gen_next(0,[])
        print("res: \n", bin_list)
        print('length:', len(bin_list))
        for bin in bin_list:
            one_comb = []
            for idx, v in enumerate(bin):
                if v:
                    one_comb.append(ar[idx])
            combs.append(one_comb)
        print("RESULT: ", combs)
s = Solution()
s.find_comb([1,2,3,4,5])
# s.find_comb([1,2,])
    