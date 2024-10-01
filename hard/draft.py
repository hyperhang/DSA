base = 27
lim = 1e9 + 7
def get_val(inp: str):
    s = 0
    for c in inp:
        s = (s*base + ord(c) - 97 + 1 ) % lim
    return s


s = 'abcd'
for idx, c in enumerate(s):
    print(idx, c)
   