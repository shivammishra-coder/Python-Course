class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the current width
            width = right - left
            
            # The height of the water is limited by the shorter bar
            current_height = min(height[left], height[right])
            
            # Update max_water if the current container holds more
            current_area = current_height * width
            if current_area > max_water:
                max_water = current_area
            
            # Move the pointer of the shorter bar inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water