class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ver = moves.count("U")
        ver -= moves.count("D")
        hor = moves.count("L")
        hor -= moves.count("R")
        if hor == 0 and ver == 0:
            return True
        return False
        