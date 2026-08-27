import heapq

class Twitter:
    def __init__(self):
        self.tweets = {}     # userId -> [(time, tweetId)]
        self.following = {}  # userId -> {followees}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        people = self.following.get(userId, set()) | {userId}
        heap = []
        for p in people:
            if p in self.tweets and self.tweets[p]:   # skip people with no tweets
                i = len(self.tweets[p]) - 1
                t, tid = self.tweets[p][i]
                heap.append((-t, tid, p, i))
        heapq.heapify(heap)

        feed = []
        while heap and len(feed) < 10:
            _, tid, p, i = heapq.heappop(heap)
            feed.append(tid)
            if i > 0:
                t, tid2 = self.tweets[p][i - 1]
                heapq.heappush(heap, (-t, tid2, p, i - 1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)