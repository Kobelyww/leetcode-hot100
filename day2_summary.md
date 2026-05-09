shangcha# Day 2 学习总结

## 今日题目

| 题号 | LeetCode | 题目 | 难度 | 核心技巧 |
|------|----------|------|------|----------|
| H03 | 3 | Longest Substring Without Repeating Characters（无重复字符的最长子串） | Medium | 滑动窗口 + 哈希表 |
| H04 | 4 | Median of Two Sorted Arrays（寻找两个正序数组的中位数） | Hard | 二分查找分割位置 |

---

## H03 - Longest Substring Without Repeating Characters（无重复字符的最长子串）

### 问题

给定一个字符串 `s`，找出其中不含有重复字符的**最长子串**的长度。注意是子串（连续），不是子序列。

### 解法：滑动窗口 + 哈希表

维护一个窗口 `[left, right]`，窗口内始终没有重复字符：

- `right` 指针不断右移，将新字符纳入窗口
- 哈希表 `seen` 记录每个字符**最近一次出现的下标**
- 当 `right` 遇到一个字符，且该字符上次出现的位置 `>= left`（在窗口内）→ 说明窗口内出现重复
- 此时将 `left` 跳到重复字符上次出现位置的**下一位**，窗口重新变得无重复
- 每一步更新最大窗口长度：`max_len = max(max_len, right - left + 1)`
- 时间复杂度 **O(n)**，空间复杂度 **O(min(n, 字符集大小))**

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    seen = {}
    max_len = 0
    left = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

### 三个容易踩的坑（来自今天的调试过程）

#### 坑 1：`max_len` 不要兼任"当前窗口长度"

错误写法在 `if` 分支里让 `max_len` 自增（`max_len += 1`），在 `else` 分支又把它归零（`max_len = 0`）。这导致 `max_len` 既当"当前长度"又当"历史最大值"，一旦归零就丢失了真正的最大值。

**正确做法**：用一个独立的变量（`cur_len` 或直接用 `right - left + 1`）表示当前窗口长度，`max_len` 只用于记录历史最大值。

#### 坑 2：`left` 不能往回跳

当遇到重复字符时，必须检查**该字符的旧位置是否在窗口内**，即 `seen[ch] >= left`。如果不加这个条件，`left` 可能会跳到比当前位置更靠前的地方，把之前因为其他重复而被排除的字符重新包回窗口。

典型反例 `"abba"`：
```
right=3, ch='a' → seen['a'] = 0, left = 2
如果直接 left = seen['a'] + 1 = 1  ← left 倒退!
窗口从 [2,3]="b" 变成 [1,3]="bba"，出现重复 b
```

#### 坑 3：更新 `seen` 和 `max_len` 不要放在分支里

即使字符"在窗口外重复"（`seen[ch] < left`），也需要更新 `seen[ch] = right` 和 `max_len`。如果只在 `if` / `elif` 分支里更新，窗口外重复的情况会静默跳过，导致 `seen` 记录过期、`max_len` 不再更新。

**正确做法**：`seen[ch] = right` 和 `max_len` 更新放在条件判断外面，每一步都执行。

---

## H04 - Median of Two Sorted Arrays（寻找两个正序数组的中位数）

### 问题

给定两个有序数组 `nums1` 和 `nums2`，找出合并后数组的中位数。要求时间复杂度 O(log(m + n))。

### 解法：二分查找分割位置

核心思路：中位数将合并后的数组平分为左右两半，我们不需要真正合并，只需要找到正确的分割线。

- 在较短数组 `nums1` 上二分，设分割点在 `i`，则另一个数组的分割点 `j = total_left - i` 自动确定
- 分割线将每个数组分成左半（最大值）和右半（最小值），得到四个值：`left1`, `right1`, `left2`, `right2`
- 正确分割的条件：`left1 <= right2` 且 `left2 <= right1`（交叉比较，左半全部 <= 右半全部）
- 不满足时调整二分：`left1 > right2` → `i` 太大，左移；否则 → `i` 太小，右移
- 越界处理：分割线在数组边界时，不存在的元素用 `-inf`（左半）或 `+inf`（右半）代替
- 总数为奇数：中位数 = `max(left1, left2)`（左半多一个）；总数为偶数：`(max(左) + min(右)) / 2`
- 时间复杂度 **O(log(min(m, n)))**，空间复杂度 **O(1)**

```python
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    total_left = (m + n + 1) // 2
    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = total_left - i

        left1  = nums1[i - 1] if i > 0 else float('-inf')
        right1 = nums1[i]     if i < m else float('inf')
        left2  = nums2[j - 1] if j > 0 else float('-inf')
        right2 = nums2[j]     if j < n else float('inf')

        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 1:
                return max(left1, left2)
            else:
                return (max(left1, left2) + min(right1, right2)) / 2
        elif left1 > right2:
            right = i - 1
        else:
            left = i + 1
```

### 关键点

- **为什么在较短数组上二分**：保证复杂度是 O(log(min(m, n)))，否则 j 可能为负数或超过 n
- **`total_left = (m + n + 1) // 2`**：这样奇数时左半多包含一个元素，中位数直接是左半最大值
- **±inf 的妙用**：统一处理边界情况，避免对 i=0、i=m、j=0、j=n 的特殊 if-else 嵌套
- **交叉比较**：不需要同数组内比较（`left1 <= right1` 天然成立因为数组有序），关键约束是跨数组的 `left1 <= right2` 和 `left2 <= right1`

---

## 今日收获

1. **滑动窗口的本质**：两个指针 `left` / `right` 维护一个满足条件的区间，`right` 负责扩展，`left` 在条件被破坏时收缩
2. **`left` 只能单调前进**：滑动窗口的 left 永远不会后退，如果代码可能让 left 变小，说明有 bug
3. **重复字符问题 = 存位置而不是存出现次数**：哈希表存字符的最近下标，遇到重复时直接跳到该位置之后，比清空重建高效得多
4. **调试时主动构造反例**：`"abba"`、`"tmmzuxt"`、`"dvdf"` 这些短字符串能快速暴露滑动窗口实现中的 corner case
5. **二分不一定用在查找具体值**：H04 中二分查找的是分割位置，而非某个确定的目标值，关键是能根据条件判断该往哪边收缩
6. **±inf 处理边界**：H03 用 ±inf 统一越界情况，避免大量 if-else 分支