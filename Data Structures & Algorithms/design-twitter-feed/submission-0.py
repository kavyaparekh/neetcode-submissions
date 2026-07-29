class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        people = self.following[userId] | {userId} #everyone this user follows + themself

        for person in people:
            if self.tweets[person]:
                idx = len(self.tweets[person]) - 1
                time, tweetId = self.tweets[person][idx]
                heap.append((-time, tweetId, person, idx))
            
        heapq.heapify(heap)
        result =[]

        while heap and len(result) < 10:
            negTime, tweetId, person, idx = heapq.heappop(heap)
            result.append(tweetId)

            if idx > 0:
                idx -=1
                time, nextTweetId = self.tweets[person][idx]
                heapq.heappush(heap, (-time, nextTweetId, person, idx))
        
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)