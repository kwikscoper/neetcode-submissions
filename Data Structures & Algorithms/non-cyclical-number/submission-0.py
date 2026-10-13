class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while True:
            numList = list(str(n))
            total = 0
            for digit in numList:
                total += int(digit) ** 2

            if total == 1:
                return True
            elif total in seen:
                return False
            else:
                n = total
                seen.add(n)

        return False