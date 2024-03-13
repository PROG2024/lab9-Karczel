"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter

class TestCounter(unittest.TestCase):

    #Singleton id
    def test_singleton(self):
        self.a = Counter()
        self.b = Counter()
        self.assertEqual(id(self.a),id(self.b)) # id is same

    #all reference, same count, not reset
    def test_same_count(self):
        self.d = Counter()
        self.c = Counter()
        self.assertNotEqual(0, self.c.count)