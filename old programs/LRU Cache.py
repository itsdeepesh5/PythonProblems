class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.capacity = capacity
        self.used_items = []
        self.size = 0
        #self.seq = 0
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.dic.get(key): 
            if key in self.used_items:
                self.used_items.remove(key)
            self.used_items.append(key)
            print('Getting',key, self.used_items,self.dic)
            return self.dic.get(key)
        else:
            return -1 
    
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        lru_key = 0
        if (not key) or (not value):
            return False
        if (len(self.dic) >= self.capacity):
            print('Execute before',key, self.used_items, self.dic)
            print(key in self.used_items) 
            print(key in self.dic.keys())
            #in Dic but never used 
            diff =set(self.dic.keys()).difference(set(self.used_items)) 
            if diff:
                print('EXECUTED NOT USED')
                del self.dic[list(diff)[0]]
            elif len(self.used_items):
                lru_key= self.used_items[0]
                del self.dic[lru_key]
                self.used_items.remove(lru_key)
            else:
                #When no item beign used , get the first one
                first_random= self.dic.keys()[0]
                del self.dic[first_random]
                self.used_items.remove(first_random)

        
        self.dic[key]= value
        self.used_items.append(key)
        print('Putting',key, self.used_items, self.dic)    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)