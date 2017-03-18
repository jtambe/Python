

class TrieNode:

    def __init__(self):
        self.children = {} # stores { 'character' : nextNode}
        self.endOfWord = False # marks if it is end of word



class Trie:

    def __init__(self):
        self.root = TrieNode()


    def Insert(self, word):
        current = self.root # start from root

        for i in range(len(word)): # insert each character
            ch = word[i]

            node = None
            if ch in current.children: # if character is in dictionary of root
                node = current.children[ch] # get the next node for current iteration character

            if node is None: # if current character not in Trie, add it
                node = TrieNode() # create an empty node
                current.children[ch] = node # append it to the current character

            current = node # proceed to next node

        current.endOfWord = True # mark last node as end of word




#driver

t = Trie()
t.Insert("abc")
t.Insert("abg")
t.Insert("abgl")