class Solution:
    def convertToCamelCase(self, s):
        words = s.split()
        if not words:
            return ""
            
        res = [words[0]]
        for i in range(1, len(words)):
            res.append(words[i].capitalize())
            
        return "".join(res)