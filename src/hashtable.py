# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # set hash value as arbitrary large prime number
        hash_value = 5381
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + char
        return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        keyHash = self._hash_mod(key)

        if self.storage[keyHash] is not None:
            previous_node = None
            current_node = self.storage[keyHash]
            while current_node is not None:
                if current_node.key == key:
                    current_node.value = value
                    return
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = LinkedPair(key, value)

        else:
            if self.count >= self.capacity:
                self.resize()
            self.storage[keyHash] = LinkedPair(key, value)
            self.count += 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        keyHash = self._hash_mod(key)
        if self.storage[keyHash] is None:
            print('Key not found')
            return
        previous_node = None
        current_node = self.storage[keyHash]
        while current_node is not None:
            if key == current_node.key:
                if previous_node is None:
                    self.storage[keyHash] = None
                    return
                previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        keyHash = self._hash_mod(key)
        if self.storage[keyHash] is not None and self.storage[keyHash].key != key:
            current_node = self.storage[keyHash]
            while current_node is not None:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next
        return self.storage[keyHash].value if self.storage[keyHash] is not None else None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = self.storage
        self.storage = [None] * self.capacity
        for node in new_storage:
            current_node = node
            while current_node is not None:
                self.insert(current_node.key, current_node.value)
                current_node = current_node.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
