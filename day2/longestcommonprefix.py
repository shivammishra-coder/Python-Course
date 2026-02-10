class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return "" 
        
        
        prefix = arr[0]
        
        for i in range(1, len(arr)):
            
            while not arr[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return "" 
                    
        return prefix