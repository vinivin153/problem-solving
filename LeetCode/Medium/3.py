class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        ss = set()
        ans = 0
        while right < len(s):
            if s[right] not in ss:
                ss.add(s[right])
                ans = max(ans, right - left + 1)
                right += 1 
            else:
                ss.remove(s[left])
                left += 1
                    
        return ans