'''
Creating a hashtable example in python.

@author: Grant Cahill
'''
"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        self.table[self.calculate_hash_value(string)] = string

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash = self.calculate_hash_value(string)
        value = self.table[hash]
        if value != None:
            return hash
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        
        # Hash equation: Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        
        if string[0] and string[1]:
            first_letter = string[0]
            second_letter = string[1]
            hash_value = (ord(first_letter) * 100) + ord(second_letter)
            return hash_value
        else:
            return -1
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
