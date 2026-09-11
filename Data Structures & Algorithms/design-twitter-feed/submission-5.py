class Twitter:

    def __init__(self):
        self.count = 0 
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count,tweetId])
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] 
        minheap = [] 

        followeeset = self.followmap[userId]
        followeeset.add(userId)

        for followee in followeeset: 
            if followee in self.tweetmap and self.tweetmap[followee]: 
                index = len(self.tweetmap[followee]) - 1 
                count, tweetId = self.tweetmap[followee][index]
                heapq.heappush(minheap,[count,tweetId,followee, index - 1])
        
        while minheap and len(res) < 10: 
            count,tweetId, followee, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0: 
                count,tweetId = self.tweetmap[followee][index]
                heapq.heappush(minheap,[count,tweetId,followee, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]: 
            self.followmap[followerId].remove(followeeId)
        
