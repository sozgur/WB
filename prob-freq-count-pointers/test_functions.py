import unittest
from construct_note import construct_note
from average_pair import average_pair, average_pair_pointer
from two_array_object import two_array_object
from same_frequency import same_frequency
from separate_positive import separate_positive
from is_subsequence import is_subsequence
from count_pairs import count_pairs
from longest_fall import longest_fall
from pivot_index import pivot_index

class TestCases(unittest.TestCase):

    def test_construct_note_function(self):
        self.assertFalse(construct_note('aa', 'abc'))
        self.assertFalse(construct_note('abcc', 'abc'))
        self.assertTrue(construct_note('aabbcc', 'bcabcaddff'))
        self.assertTrue(construct_note('abc', 'dcba'))

    def test_function_avarege_pair(self):
        self.assertFalse(average_pair([], 4))
        self.assertFalse(average_pair([-1, 0, 3, 4, 5, 6], 4.1))
        self.assertTrue(average_pair([1, 2, 3], 2.5))
        self.assertTrue(average_pair([1, 3, 3, 5, 6, 7, 10, 12, 19], 8))

    def test_function_average_pair_pointer(self):
        self.assertFalse(average_pair_pointer([], 4))
        self.assertFalse(average_pair_pointer([-1, 0, 3, 4, 5, 6], 4.1))
        self.assertTrue(average_pair_pointer([1, 2, 3], 2.5))
        self.assertTrue(average_pair_pointer([1, 3, 3, 5, 6, 7, 10, 12, 19], 8))
    
    def test_two_array_object_function(self):
        self.assertEqual(two_array_object(['a', 'b', 'c', 'd'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3, 'd': None})
        self.assertEqual(two_array_object(['a', 'b', 'c'], [1, 2, 3, 4]), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(two_array_object(['x', 'y', 'z'], [1, 2]), {'x': 1, 'y': 2, 'z': None})


    def test_same_frequency_fucntion(self):
        self.assertTrue(same_frequency(182, 281))
        self.assertTrue(same_frequency(3589578, 5879385))
        self.assertFalse(same_frequency(22,222))
        self.assertFalse(same_frequency(34,14))

    def test_separete_positive_function(self):
        self.assertTrue(separate_positive([2, -1, -3, 6, -8, 10])[0] > 0 )
        self.assertTrue(separate_positive([5, 10, -15, 20, 25])[-1] < 0)
        self.assertEqual(separate_positive([-5, 5]), [5, -5])
        self.assertEqual(separate_positive([1, 2, 3]), [1, 2, 3])

    def test_is_subsequence_function(self):
        self.assertTrue(is_subsequence('hello', 'hello world'))
        self.assertTrue(is_subsequence('sing', 'sting'))
        self.assertTrue(is_subsequence('abc', 'abracadabra'))
        self.assertFalse(is_subsequence('abc', 'acb'))

    def test_count_pairs(self):
        self.assertEqual(count_pairs([3,1,5,4,2,10], 6), 2)
        self.assertEqual(count_pairs([10,4,8,2,6,0], 10), 3)
        self.assertEqual(count_pairs([4,6,2,7], 10), 1)
        self.assertEqual(count_pairs([1,2,3,4,5], 10), 0)
        self.assertEqual(count_pairs([1,2,3,4,5], -3), 0)
        self.assertEqual(count_pairs([0,-4], -4),1)
        self.assertEqual(count_pairs([1,2,3,0,-1,-2] ,0), 2)

    def test_longest_fall_function(self):
        self.assertEqual(longest_fall([5, 3, 1, 3, 0]), 3)
        self.assertEqual(longest_fall([2, 2, 1]), 2)
        self.assertEqual(longest_fall([2, 2, 2]), 1)
        self.assertEqual(longest_fall([5, 4, 4, 4, 3, 2]) ,3)
        self.assertEqual(longest_fall([9, 8, 7, 6, 5, 6, 4, 2, 1]), 5)
        self.assertEqual(longest_fall([]),0)
        self.assertEqual(longest_fall([1]),1)

    def test_pivot_index_function(self):
        self.assertEqual(pivot_index([1,2,1,6,3,1]),3)
        self.assertEqual(pivot_index([5,2,7]),-1)
        self.assertEqual(pivot_index([-1,3,-3,2]),1)