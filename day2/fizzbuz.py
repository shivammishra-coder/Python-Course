class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        for i in range(1, n + 1):
            # Check for divisibility by both 3 and 5 first
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                # Numbers must be returned as strings
                answer.append(str(i))
                
        return answer