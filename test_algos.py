import unittest
from algos import A

class TestAlgos(unittest.TestCase):

    def count_li(self, r_list):
        count = 0
        for i in r_list:
            count += 1
        return count

    def test_random_list(self):
        x = A()
        list_lengths = [10000, 100, 666]
        for list_length in list_lengths:
            test_list = x._random_list(list_length)
            self.assertEquals(self.count_li(test_list), list_length)
            for i in test_list:
                self.assertTrue(type(i) is int)

if __name__ == '__main__':
    unittest.main()
