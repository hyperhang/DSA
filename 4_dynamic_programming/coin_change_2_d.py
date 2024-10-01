import copy
import logging

# Configure logging
logging.basicConfig(filename='output2.txt', level=logging.INFO, format='%(message)s')

class Solution:
    count = 0
    pt = set()
    def change(self, amount: int, coins: list[int]) -> int:
        amount = 500
        coins = [1,2,5]
        
        # amount = 3
        # coins = [2]
        
        # amount = 500
        # coins = [1,2,5]
        
        coins.sort()
        def check(coin_i, _amount, ar):
            if _amount < 0:
                return
            logging.info(f"----\ncheck({coin_i}, {_amount})")
            if _amount == 0:
                self.count += 1
                # ar.append([-111,-111])
                logging.info(f"_amount : 0, count += 1, count = {self.count}")
                logging.info(">>> phuong trinh la: ")
                _t = ""
                for ele in ar:
                    _t += f"{ele[1]}*c_{ele[0]} + "
                if _t in self.pt:
                    logging.info(f"bi lap lai: {_t}")
                self.pt.add(_t)    
                logging.info(_t)
                return
            if coin_i == 0 :
                if _amount % coins[coin_i] == 0 :
                    self.count += 1
                    ar.append([coin_i, _amount//coins[coin_i]])
                    # ar.append([-111,-111])
                    logging.info(f"idx: 0, count += 1, count = {self.count}")
                    logging.info("\n>>> phuong trinh la: ")
                    _t = ""
                    for ele in ar:
                        _t += f"{ele[1]}*c_{ele[0]} + "
                    logging.info(_t)
                    
                    if _t in self.pt:
                        logging.info(f"bi lap lai: {_t}")
                    self.pt.add(_t)            
                            
                    logging.info("\n>>>\n")                  
                return
            for i in range(0, amount//coins[coin_i]+1):   
                logging.info(f"i: {i}")
                _ar = copy.deepcopy(ar)
                _ar.append([coin_i,i])

                logging.info(f"check({coin_i - 1}, {_amount - i*coins[coin_i]})")                 
                check(coin_i - 1, _amount - i*coins[coin_i], _ar )
        ar = []
        check(len(coins)-1, amount, ar)   
        logging.info(f"\nFinal: {self.count}")
        return self.count

s = Solution()
s.change(None, None)