class Solution:
    first_smallest_num = 10**20
    first_smallest_diff = 10**20
    second_smallest_num = 10**20
    second_smallest_diff = 10**20
    def make_palindrome(self, first_digits: str, length: int, filled : str = '0'):
            if len(first_digits)*2-1 == length:
                return int(first_digits+ ''.join([first_digits[d] for d in range(len(first_digits)-2,-1,-1) ]))
            else:
                return int(first_digits+ filled*(length-len(first_digits)*2 ) + ''.join([first_digits[d] for d in range(len(first_digits)-1,-1,-1) ]))
    
    def is_palindrome(self, n:str):
        if self.make_palindrome(n[:(len(n)+1)//2], len(n)) == int(n):
            return True
        return False
    
    def nearestPalindromic(self, n: str) -> str:

        def update_value(first_digits: str, n_str: str, palindrome: int = None, filled : str = '0'):
            _num = 0
            if palindrome:
                _num = palindrome
            else:
                _num = self.make_palindrome(first_digits, len(n_str), filled)
            print("update_value: ", _num)
            if abs(_num - int(n_str)) < self.first_smallest_diff:
                print("case 1")
                self.second_smallest_diff = self.first_smallest_diff
                self.second_smallest_num = self.first_smallest_num
                
                self.first_smallest_diff = abs(_num - int(n_str))
                self.first_smallest_num = _num
            
            elif abs(_num - int(n_str)) == self.first_smallest_diff and _num < self.first_smallest_num:
                print("case 2")
                self.first_smallest_num = _num
                
            elif abs(_num - int(n_str)) < self.second_smallest_diff and _num != self.first_smallest_num:
                print("case 3")
                self.second_smallest_diff = abs(_num - int(n_str))
                self.second_smallest_num = _num
                
            elif abs(_num - int(n_str)) ==  self.second_smallest_diff and _num < self.second_smallest_num:
                print("case 4")
                self.second_smallest_num = _num
            print("Update Global: ")
            print("1st smallest num, diff = ", self.first_smallest_num,",", self.first_smallest_diff)
            print("2nd smallest num, diff = ",self.second_smallest_num,",", self.second_smallest_diff)
            print("-"*30)

            
        def check_num(index, n_str:str):
            print(f"check_num: idx={index}, n={n_str}")
            # increase 1 on index-th 
            print("increase 1")
            if n_str[index] == '9':
                pass
            else:
                _first_digits = n_str[:index] + str(int(n_str[index])+1)
                update_value(_first_digits, n_str, None, filled = '0')
            
            # decrease 1 on index-th 
            print("decrease 1")
            if n_str[index] == '0':
                pass
            else:
                _first_digits = n_str[:index] + str(int(n_str[index])-1)
                update_value(_first_digits, n_str, None, filled = '9')

            # keep index-th value
            print("keep ind")
            _first_digits = n_str[:index+1]
            update_value(_first_digits, n_str, None)
            
            
        if len(n) == 1:
            print("RESUTL : ", max(0, int(n)-1) )
            return str(max(0, int(n)-1))
        
        _num, _diff = 0, 0,
        # if n is 1xxx or n is 9xxx:
        if n[0]=='1':
            _num = '9'*(len(n)-1)
            update_value(None,n, int(_num))
                
        if n[len(n)-1] == '9':
            _num = '1'+ '0'*(len(n)-1) +'1'
            update_value(None, n, int(_num))

        # else:
        if len(n) % 2 == 0:
            for idx in range(len(n)//2):
                check_num(idx, n)
        else:
            for idx in range(len(n)//2+1):
                check_num(idx, n)     
                
        print("RESULT: ", self.first_smallest_num, self.second_smallest_num)
        if self.is_palindrome((n)):
            print("input is : palindrom")
            if int(n) == self.first_smallest_num:
                return str(self.second_smallest_num)
            else:
                return str(self.first_smallest_num)
        else:
            print("input is : NOT palindrom")
            return str(self.first_smallest_num)
    
    

s = Solution()
# print(s.make_palindrome("2", 2))
# s.nearestPalindromic("145")
# s.nearestPalindromic("14556")
# s.nearestPalindromic("141")
# s.nearestPalindromic("1441")
# print(s.nearestPalindromic("999"))
# print(s.nearestPalindromic("11011"))
print(s.nearestPalindromic("9009"))
# s.nearestPalindromic("101")
# print(s.nearestPalindromic("11"))
# print(s.nearestPalindromic("88"))
# print(s.nearestPalindromic("101"))
# s.nearestPalindromic("1")
# s.nearestPalindromic("0")
# s.nearestPalindromic("123")
# s.nearestPalindromic("1000999")

