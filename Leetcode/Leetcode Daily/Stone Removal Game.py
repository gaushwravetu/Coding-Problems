class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_to_remove = 10
        turn = 0
        while n > 0:
            if n < stones_to_remove:
                return turn == 1
            n -= stones_to_remove
            stones_to_remove -= 1
            turn = 1 - turn
    
        return turn == 1



        