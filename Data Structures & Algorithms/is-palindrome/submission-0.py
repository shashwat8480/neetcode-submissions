class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = [] 

        for c in s: 
            if c.isalnum(): 
                word.append(c.lower())
        
        original = word[:]

        self.reverse(word)

        return original == word
    
    def reverse(self,s): 
        left = 0 
        right = len(s) -1 

        while left < right: 
            temp = s[left]
            s[left] = s[right]
            s[right] = temp 
        
            left += 1 
            right -= 1
        


        

    
        