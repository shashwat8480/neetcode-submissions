class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): 
            return False 
        
        hashmap = {} 

        for i in range(len(s)): 
            hashmap[s[i]] = 1 + hashmap.get(s[i],0)
        
        for i in range(len(t)): 
            hashmap[t[i]] = hashmap.get(t[i],0) - 1 
        
        for count in hashmap.values(): 
            if count != 0: 
                return False 
        
        return True 
      