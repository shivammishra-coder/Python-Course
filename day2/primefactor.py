class Solution:
    def primeFac(self, n):
        res = []
        
        
        if n % 2 == 0:
            res.append(2)
            while n % 2 == 0:
                n //= 2
        
        
        i = 3
        while i * i <= n:
            if n % i == 0:
                res.append(i)
                
                while n % i == 0:
                    n //= i
            i += 2
        
        
        if n > 1:
            res.append(n)
            
        return res
