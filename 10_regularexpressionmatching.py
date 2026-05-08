"""
LeetCode 10. 正则表达式匹配 (Regular Expression Matching)

题目描述：
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

- '.' 匹配任意单个字符
- '*' 匹配零个或多个前面的那一个元素
- 匹配应覆盖整个字符串 s，而不是部分字符串

示例 1:
输入: s = "aa", p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入: s = "aa", p = "a*"
输出: true
解释: '*' 表示可以匹配零个或多个前面的元素 'a'，因此重复 'a' 一次后 "aa" 匹配。

示例 3:
输入: s = "ab", p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个任意字符（'.'）。

提示:
- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s 只包含小写英文字母
- p 只包含小写英文字母，以及字符 '.' 和 '*'
- 保证每次出现字符 '*' 时，前面都匹配到有效的字符
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        动态规划法

        核心思路：
        dp[i][j] 表示 s 的前 i 个字符与 p 的前 j 个字符是否能匹配。

        转移方程：
        - p[j-1] 是普通字符或 '.': dp[i][j] = 当前字符匹配 and dp[i-1][j-1]
        - p[j-1] 是 '*': 分两种情况
          a) '*' 匹配零次（忽略前一个字符和 '*'）：dp[i][j] = dp[i][j-2]
          b) '*' 匹配一次或多次（当前字符匹配前一个字符）：dp[i][j] = dp[i-1][j]

        时间复杂度 O(m * n)，空间复杂度 O(m * n)
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 空串匹配空模式
        dp[0][0] = True

        # 初始化：空串 s 匹配模式 p 的前缀（只有 a*b*c* 这类可能匹配空串）
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]        # '*' 让前一个字符出现零次

        # 填充 DP 表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 情况 a：'*' 匹配零次，跳过前一个字符和 '*'
                    dp[i][j] = dp[i][j - 2]
                    # 情况 b：'*' 匹配一次或多次（前提是当前 s 字符匹配 '*' 前面的字符）
                    if not dp[i][j] and self._matches(s[i - 1], p[j - 2]):
                        dp[i][j] = dp[i - 1][j]    # s 去掉最后一个字符，还能继续用这个 '*'
                else:
                    # 普通字符或 '.'：当前字符必须匹配，然后看前面的子串
                    if self._matches(s[i - 1], p[j - 1]):
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]

    def _matches(self, a: str, b: str) -> bool:
        """判断单个字符是否匹配：相等 或 模式字符是 '.'"""
        return a == b or b == '.'


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    # 示例 1
    assert s.isMatch("aa", "a") == False

    # 示例 2
    assert s.isMatch("aa", "a*") == True

    # 示例 3
    assert s.isMatch("ab", ".*") == True

    # 额外测试：复杂模式
    assert s.isMatch("aab", "c*a*b") == True

    # 额外测试：不匹配
    assert s.isMatch("mississippi", "mis*is*p*.") == False

    # 额外测试：空串匹配
    assert s.isMatch("", ".*") == True
    assert s.isMatch("", "a*") == True
    assert s.isMatch("", "a") == False

    # 额外测试：无 '*'
    assert s.isMatch("abc", "a.c") == True
    assert s.isMatch("abc", "abc") == True
    assert s.isMatch("abc", "abd") == False

    print("✅ 所有测试用例通过！")