import copy

class Solution:
    count = 0
    def change(self, amount: int, coins: list[int]) -> int:
        amount = 500
        coins = [1,2,5]
        
        # amount = 3
        # coins = [2]
        
        # amount = 500
        # coins = [1,2,5]
        
        coins.sort()
        def check(coin_i, _amount, ar):
            print(f"----\ncheck({coin_i}, {_amount})")
            if _amount == 0:
                self.count += 1
                # ar.append([-111,-111])
                print("_amount : 0, count += 1, count = ", self.count)
                print(">>> phuong trinh la: ")
                for ele in ar:
                    print(f"{ele[1]}*c_{ele[0]} + ", end="")
                return
            if coin_i == 0 :
                if _amount % coins[coin_i] == 0 :
                    self.count += 1
                    ar.append([coin_i, _amount//coins[coin_i]])
                    # ar.append([-111,-111])
                    print("idx: 0, count += 1, count = ", self.count)
                    print("\n>>> phuong trinh la: ")
                    for ele in ar:
                        print(f"{ele[1]}*c_{ele[0]} + ", end="")  
                    print("\n>>>\n")                  
                return
            for i in range(0, amount//coins[coin_i]+1):   
                print("i: ", i)
                _ar = copy.deepcopy(ar)
                _ar.append([coin_i,i])

                print(f"check({coin_i - 1}, {_amount - i*coins[coin_i]})")                 
                check(coin_i - 1, _amount - i*coins[coin_i], _ar )
        ar = []
        check(len(coins)-1, amount, ar)   
        print("\nFinal: ", self.count)
        return self.count

s = Solution()
s.change(None, None)
# c = 0
# for x in range(0,501):
#     for y in range(0,251):
#         for z in range(0, 101):
#             if x + 2*y + z*5 == 500:
#                 c += 1
# print("Count: ", c)


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        def check(coin_i, _amount):
            if _amount == 0:
                
                return 1
            if coin_i == 0 :
                if _amount % coins[coin_i] == 0 :
                    return 1
                else:
                    return 0
            total_combinations = 0
            for i in range(0, amount//coins[coin_i]+1):                 
                total_combinations += check(coin_i - 1, _amount - i*coins[coin_i])
            return total_combinations
        return check(len(coins)-1, amount)   
# amount = 5
# coins = [1,2,5]
# amount = 500
# coins = [1,2,5]
# s = Solution()
# print(s.change(amount, coins))