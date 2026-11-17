class Node:
    def __init__(self):
        self.children = {}
        self.res = []

class Trie:
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
            curr.res.append(word)
            curr.res.sort()
            if len(curr.res) > 3:
                curr.res.pop(3)

    def search(self, word):
        lst = []
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
                lst.append(curr.res)
            else:
                lst.append([])
                curr = Node()   # empty node: every later char misses too
        return lst

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tree = Trie()
        for word in products:
            tree.addWord(word)
        return tree.search(searchWord)