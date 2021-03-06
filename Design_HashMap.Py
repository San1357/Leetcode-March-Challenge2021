''' Problem : DESIGN HASHMAP '''


#CODE :


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.block = 1000
        self._map = [] 
        self.len = 0 
        self.incr()
        
    def incr(self) :
        self._map += [-1] * self.block
        self.len += self.block
        
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        while key > self.len:
            self.incr()
            
        self._map[key] = value

        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key < self.len:
            return self._map[key]
        return -1
    

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key < self.len:
            self._map[key] = -1
            
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
