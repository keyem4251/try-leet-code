#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while True:
            if i * i > x:
                return i - 1

            i += 1
# @lc code=end

