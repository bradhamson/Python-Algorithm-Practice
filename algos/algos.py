from random import random

class A(object):

    def __init__(self):
        pass

    def _random_list(self, list_len):
        """
        Takes desired list length and returns a list of random integers at the
        correct length
        """
        r = [int(random()*1000) for i in xrange(list_len)]
        return r

    def bubble_sort(self):
        pass
