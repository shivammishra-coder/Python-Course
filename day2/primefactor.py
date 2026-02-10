class Solution:
    def primeFac(self, n):
        res = []
        
        # 1. Check for the smallest prime factor, 2
        if n % 2 == 0:
            res.append(2)
            while n % 2 == 0:
                n //= 2
        
        # 2. Check for odd factors from 3 to sqrt(n)
        i = 3
        while i * i <= n:
            if n % i == 0:
                res.append(i)
                # Remove all occurrences of this prime factor
                while n % i == 0:
                    n //= i
            i += 2
        
        # 3. If n is still > 1, the remaining n is a prime factor
        if n > 1:
            res.append(n)
            
        return res