"""
Design HashMap
https://leetcode.com/problems/design-hashmap/
"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.elements[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.elements.get(key, -1)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        try:
            del self.elements[key]
        except:
            pass

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
