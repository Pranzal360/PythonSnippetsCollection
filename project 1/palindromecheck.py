class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = 0
        x_val = x
        value = 0
        while x !=0:
            mod = x % 10
            value = value * 10 + mod
            x = x // 10
            n +=1
            print(n)
        if x_val == value:
            return True
        else:
            return False

a = Solution()
a.isPalindrome(-121)