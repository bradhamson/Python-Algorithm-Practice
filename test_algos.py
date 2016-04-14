import unittest
from algos import A

class TestAlgos(unittest.TestCase):

    def count_li(self, r_list):
        count = 0
        for i in r_list:
            count += 1
        return count

    def test_random_list(self):
        x = A()._random_list(10000)
        y = A()._random_list(100)
        z = A()._random_list(666)
        self.assertEquals(self.count_li(x), 10000)
        self.assertEquals(self.count_li(y), 100)
        self.assertEquals(self.count_li(z), 666)
        instances = [x, y, z]
        for inst in instances:
            for i in inst:
                self.assertTrue(type(i) is int)

if __name__ == '__main__':
    unittest.main()
