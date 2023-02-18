#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for bracket in s:
            if bracket in ["(", "[", "{"]:
                l.append(bracket)
            else:
                if bracket == ")" and l[-1] == "(":
                    l.pop(-1)
                elif bracket == "]" and l[-1] == "[":
                    l.pop(-1)
                elif bracket == "}" and l[-1] == "{":
                    l.pop(-1)

        return True if not l else False
# @lc code=end

