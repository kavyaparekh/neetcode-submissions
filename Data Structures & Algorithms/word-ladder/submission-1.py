class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set()
        for w in wordList:
            words.add(w)
        if beginWord not in words   :
            words.add(beginWord)

        adj = defaultdict(list)
        
        for word in words:
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in words:
                        adj[word].append(newWord)
        
        q = deque()
        q.append(beginWord)
        vis = set()
        vis.add(beginWord)
        cnt = 1
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return cnt
                for nei in adj[node]:
                    if nei not in vis:
                        q.append(nei)
                        vis.add(nei)
            cnt+=1
        return 0
