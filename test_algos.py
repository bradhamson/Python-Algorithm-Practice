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

    def test_bubble_sort(self):
        x = A()
        test_list = x._random_list(100)
        x.bubble_sort(test_list)
        length = len(test_list)
        for i in xrange(length-1):
            self.assertTrue(test_list[i] <= test_list[i+1])

if __name__ == '__main__':
    unittest.main()
