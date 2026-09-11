class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char,cnt in count.items()]
        heapq.heapify(maxHeap)

        res = [] 
        q = deque()

        while maxHeap: 
            count, char = heapq.heappop(maxHeap)
            res.append(char)
            count += 1 

            q.append([count,char])
            if len(q) >= 2: 
                oldcount,oldchar = q.popleft()
                if oldcount != 0: 
                    heapq.heappush(maxHeap,[oldcount,oldchar]) 
        
        if len(res) != len(s): 
            return ""
        
        return "".join(res)
            