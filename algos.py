from random import random

class A(object):

    def __init__(self):
        pass

    def random_list(self, list_len):
        """
        Takes desired list length and returns a list of random integers at the
        correct length to test sorting algos
        """
        r = [int(random()*1000) for i in xrange(list_len)]
        return r

    def bubble_sort(self, u_list):
        length = len(u_list) - 1
        sort = False
        while not sort:
            sort = True
            for i in xrange(length):
                if u_list[i] > u_list[i+1]:
                    sort = False
                    u_list[i], u_list[i+1] = u_list[i+1], u_list[i]

    def merge_sort(self, u_list):
        length = len(u_list)
        if length > 1:
            left = u_list[:(length/2)]
            right = u_list[(length/2):]
            self.merge_sort(left)
            self.merge_sort(right)

