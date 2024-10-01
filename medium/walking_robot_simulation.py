from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocks = set()
        for obs in obstacles:
            blocks.add(f"{obs[0]}-{obs[1]}")
        direction = ['n', 'e', 's', 'w']
        
        norm_commands = []
        for cmd in commands:
            if cmd < 0:
                norm_commands.append(cmd)
            else:
                norm_commands += [1]*cmd

        def check_obs(x, y):
            return True if f"{x}-{y}" in blocks else False
        
        def move(cmd, maxxx, dir_idx, x, y):
            if cmd == -2:
                dir_idx = (dir_idx+3)%4
            elif cmd == -1:
                dir_idx = (dir_idx+1)%4
            else:
                # cmd == 1
                if dir_idx == 0:
                    if not check_obs(x , y+1):
                        y += 1
                elif dir_idx == 1:
                    if not check_obs(x+1, y):
                        x += 1
                        
                elif dir_idx == 2:
                    if not check_obs(x , y-1):
                        y -= 1
                else:
                    if not check_obs(x-1, y):
                        x -= 1
            maxxx = max(maxxx,  x*x + y*y)
            return (maxxx, dir_idx, x, y)

        ma = 0
        dir_idx = 0
        x, y = 0, 0
        for cmd in norm_commands:
            ma, dir_idx, x, y = move(cmd, ma, dir_idx, x, y)
        
        return ma
    
s = Solution()

commands = [4,-1,3]
obstacles = []

commands = [4,-1,4,-2,4]
obstacles = [[2,4]]

commands = [6,-1,-1,6]
obstacles = []

print(s.robotSim(commands, obstacles))