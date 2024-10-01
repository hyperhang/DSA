class Solution:
    def myAtoi(self, s: str) -> int:
        nstr = ""
        s = s.strip()
        max_lim = str(2**31 - 1)
        min_lim = str(2**31)
        if len(s) == 0:
            return 0
        if not (s[0] == '-' or s[0] == '+' or ord('9') >= ord(s[0]) >= ord('0') ) :
            return 0
        signed = 1
        if s[0] == '-':
            signed = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        elif ord('9') >= ord(s[0]) >= ord('0'):
            pass
        else:
            return 0
        
        for c in s:
            if ord('9') >= ord(c) >= ord('0'):
                nstr += c
            else:
                break
            
        i = 0
        while i < len(nstr) and nstr[i] == '0':
            i += 1
        nstr = nstr[i:]
        print(f"nstr: {nstr}, signed: {signed}")
        if len(nstr) == 0:
            return 0
        if signed >= 0:
            if len(nstr) < len(max_lim):
                return int(nstr)
            elif len(nstr) == len(max_lim):
                if nstr > max_lim:
                    return int(max_lim)
                else:
                    return int(nstr)
            else:
                return int(max_lim)
        else:
            if len(nstr) < len(min_lim):
                return -int(nstr)
            elif len(nstr) == len(min_lim):
                if nstr > max_lim:
                    return -int(min_lim)
                else:
                    return -int(nstr)
            else:
                return -int(min_lim)

sol = Solution()
s = '42'
s = '-042'
s = '1337c0d3'
s = '0-1'
# s = 'words and 93'
# s = '+002147483647'
# s = '+002147483645'
# s = '-002147483645'
# s = '-002147483649'
# s = '-0098'
s = '-+12'
s = ''
print(sol.myAtoi(s))
        
        
