class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids: 
            alive = True 

            while stack and asteroid < 0 and stack[-1] > 0 and alive:
                if stack[-1] < -asteroid: 
                    stack.pop() 
                    continue 
                
                elif stack[-1] == -asteroid: 
                    stack.pop()
                    alive = False 
                
                else: 
                    alive = False 
            
            if alive:
                stack.append(asteroid)
        
        return stack
        