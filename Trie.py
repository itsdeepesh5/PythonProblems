class Trie:
    def __init__(self):
        self.root_node={}

    def add_word(self, word):
        if len(word) == 0:
            return 0

        current_node= self.root_node
        is_new_word= False
        for char in word:
            if char not in current_node:
                current_node[char]= {}
                is_new_word=True
            current_node= current_node[char]

        if "End or Word" not in current_node:
            current_node["End of Word"] = {}
            
        return is_new_word

    def printTrie(self, v=None):
        if not v:
            current_node= self.root_node
        else:        
            current_node= v.root_node
        for k,v in current_node.items():
            print(k, v)
            
t= Trie()
t.add_word('Deepesh')
t.add_word('deep')

print(t.printTrie())
