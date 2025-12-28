class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        if x >= 0: 
            pass
        else:
            string = string[1:]
        string = string[::-1]
        num = int(string)

        if x < 0:
            num = -1 * num

        low = -1 * (2 ** 31)
        high = (2 ** 31) - 1

        if num < low or num > high :
            return 0
        
        return num