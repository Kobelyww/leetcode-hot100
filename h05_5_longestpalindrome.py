"""
LeetCode 5. 最长回文子串 (Longest Palindromic Substring)

题目描述：
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

示例 1:
输入: s = "babad"
输出: "bab"
解释: "aba" 同样是符合题意的答案。

示例 2:
输入: s = "cbbd"
输出: "bb"

提示:
- 1 <= s.length <= 1000
- s 仅由数字和英文字母组成
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        中心扩展法

        核心思路：
        回文串有两种形式：奇数长度（中心是单个字符，如 "aba"）和偶数长度
        （中心在两个字符之间，如 "abba"）。遍历每个可能的中心，用双指针向
        两边扩展，相等就继续，不相等就停止。

        关键细节：
        - 对每个位置 i，同时检查奇数（中心 i）和偶数（中心 i,i+1）两种情形
        - 记录最长回文的起始下标 start 和长度 max_len，遇到更长的就更新
        - 最后用 s[start:start+max_len] 截取结果，避免每次构造子串

        时间复杂度 O(n^2)，空间复杂度 O(1)
        """
        n = len(s)
        start = 0                              # 最长回文的起始下标
        max_len = 1                            # 最长回文的长度（至少为1，单字符是回文）

        for i in range(n):
            # --- 奇数长度回文：中心是 s[i] ---
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                cur_len = right - left + 1
                if cur_len > max_len:          # 发现更长的回文，更新记录
                    max_len = cur_len
                    start = left
                left -= 1                      # 左指针向外扩展
                right += 1                     # 右指针向外扩展

            # --- 偶数长度回文：中心在 s[i] 和 s[i+1] 之间 ---
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                cur_len = right - left + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = left
                left -= 1
                right += 1

        return s[start:start + max_len]        # 根据记录截取结果子串


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    # 示例 1
    result1 = s.longestPalindrome("babad")
    assert result1 in ("bab", "aba"), f"Expected 'bab' or 'aba', got '{result1}'"

    # 示例 2
    assert s.longestPalindrome("cbbd") == "bb"

    # 额外测试：单字符
    assert s.longestPalindrome("a") == "a"

    # 额外测试：全部相同
    assert s.longestPalindrome("aaaa") == "aaaa"

    # 额外测试：无长回文
    assert s.longestPalindrome("abc") in ("a", "b", "c")

    print("✅ 所有测试用例通过！")
