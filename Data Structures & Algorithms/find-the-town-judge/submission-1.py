class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #judge has 0 outgoing, n - 1 incoming 

        outgoing = {}
        incoming = {}

        for source,dest in trust: 
            outgoing[source] = 1 + outgoing.get(source,0)
            incoming[dest] = 1 + incoming.get(dest,0)
        
        for i in range(1,n+1): 
            if outgoing.get(i,0) == 0 and incoming.get(i,0) == n - 1: 
                return i  

        return -1
