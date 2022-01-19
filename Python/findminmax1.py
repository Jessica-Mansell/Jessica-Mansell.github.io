class Solution:
    def __init__(self, input):
        self.input = input

    def find_min_element(self):
        smallest = None

        for elem in self.input:
            if(smallest == None or elem < smallest):
                smallest = elem
        return smallest

    def find_max_element(self):
        biggest = None

        for elem in self.input:
            if(biggest == None or elem > biggest):
                biggest = elem
        return biggest

my_solution = Solution(input = [3, 1, 2, 7, -1, 0])
smallest_item = my_solution.find_min_element()
biggest_item = my_solution.find_max_element()
print(smallest_item)
print(biggest_item)


#Unit test below
import unittest

class SolutionTest(unittest.TestCase):

    def test_find_min_element(self):
        solution = Solution(input=[1, 2, 3, 4, 5])
        result = solution.find_min_element()
        self.assertEqual (1, result)

unittest.main()
