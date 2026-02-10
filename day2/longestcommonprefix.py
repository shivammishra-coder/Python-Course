class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return "-1"
        
        arr.sort()
        
        first = arr[0]
        last = arr[-1]
        
        i = 0
        min_len = min(len(first), len(last))
        
        while i < min_len and first[i] == last[i]:
            i += 1
            
        res = first[:i]
        
        return res if res else "-1"