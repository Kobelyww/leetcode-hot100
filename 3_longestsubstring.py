"""
LeetCode 3. 无重复字符的最长子串 (Longest Substring Without Repeating Characters)

题目描述：
给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是子串的长度，"pwke" 是一个子序列，不是子串。

提示:
- 0 <= s.length <= 5 * 10^4
- s 由英文字母、数字、符号和空格组成
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑动窗口 + 哈希表

        核心思路：
        维护一个不含重复字符的窗口 [left, right]，用哈希表记录每个字符
        最近一次出现的下标。当 right 右移遇到重复字符时，left 直接跳到
        重复字符上次出现位置 + 1，窗口内就永远不会有重复。

        关键细节：
        - 判断重复时加了 `last_index[ch] >= left` 条件：字符可能在整个字符串
          中重复出现过，但如果上次出现的位置已经在窗口左边界 left 之前，
          就不算窗口内的重复，不需要移动 left
        - 窗口长度 = right - left + 1

        时间复杂度 O(n)，空间复杂度 O(min(n, 字符集大小))
        """
        last_index = {}                        # 字符 → 最近一次出现的下标
        left = 0                               # 窗口左边界
        max_len = 0                            # 记录窗口达到的最大长度

        for right, ch in enumerate(s):         # right 是窗口右边界，不断右移
            # 当前字符在窗口内重复出现 → 左边界跳到重复位置的下一位
            if ch in last_index and last_index[ch] >= left:
                left = last_index[ch] + 1
            last_index[ch] = right             # 更新字符最近一次出现位置
            max_len = max(max_len, right - left + 1)  # 更新最大窗口长度

        return max_len


# ========== 测试用例 ==========
if __name__ == '__main__':
    s = Solution()

    # 示例 1
    assert s.lengthOfLongestSubstring("abcabcbb") == 3

    # 示例 2
    assert s.lengthOfLongestSubstring("bbbbb") == 1

    # 示例 3
    assert s.lengthOfLongestSubstring("pwwkew") == 3

    # 额外测试：空字符串
    assert s.lengthOfLongestSubstring("") == 0

    # 额外测试：全部不重复
    assert s.lengthOfLongestSubstring("abcdef") == 6

    # 额外测试：包含空格和符号
    assert s.lengthOfLongestSubstring("a b c a") == 3  # 最长无重复子串: "a b" / "b c" / "c a"

    print("✅ 所有测试用例通过！")