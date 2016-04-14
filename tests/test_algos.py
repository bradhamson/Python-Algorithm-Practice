import unittest
from algos import A

class TestAlgos(unittest.TestCase):

    def __init__(self):
        self.test1 = A()
        self.test2 = A()
        self.test3 = A()

    def count_li(self, r_list):
        count = 0
        for i in r_list:
            count += 1
        return count

    def test_random_list(self):
        x = self.test1._random_list(10000)
        y = self.test2._random_list(100)
        z = self.test3._random_list(666)

        self.assertEquals(self.count_li(x), 10000)
        self.assertEquals(self.count_li(y), 100)
        self.assertEquals(self.count_li(z), 666)

if __name__ == '__main__':
    unittest.main()
