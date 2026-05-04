class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.endOfWord = True
        
    def search(self, word: str) -> bool:
        def helper(word, curr):
            for i,char in enumerate(word):
                if char == '.':
                    return any(helper(word[i+1:], curr.children[x]) for x in curr.children)
                if char not in curr.children:
                    return False
                curr = curr.children[char]
            return curr.endOfWord
        
        return helper(word, self.root)
            
                

                
        
