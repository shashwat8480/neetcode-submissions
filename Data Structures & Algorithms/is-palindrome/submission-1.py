class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower() 

        new_string = ""

        for char in s: 
            if char.isalnum(): 
                new_string += char 
        
        return new_string == self.reverse(new_string)
    

    def reverse(self,s): 
        s = list(s)
        left = 0 
        right = len(s) - 1 

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp 

            left += 1 
            right -= 1 
        
        return "".join(s)
       

    
        