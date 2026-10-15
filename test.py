import unittest
import u4

class TestStringProcessor(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(u4.reverse("Hello world"), "dlrow olleH")
        self.assertEqual(u4.reverse("Python"), "nohtyP")
        self.assertEqual(u4.reverse(""), "")
        self.assertNotEqual(u4.reverse("Hello world"), "Hello world")
        self.assertIsInstance(u4.reverse("Hello world"), str)

    def test_count_vowels(self):
        self.assertEqual(u4.count_vowels("Hello world"), 3)
        self.assertIsInstance(u4.count_vowels("Hello world"), int)
        self.assertRaises(TypeError, u4.count_vowels, None)
        self.assertNotEqual(u4.count_vowels("Python"), 3)
        self.assertEqual(u4.count_vowels("This is a test sentence."), 7)

    def test_count_words(self):
        self.assertEqual(u4.count_words("Python is great"), 3)
        self.assertEqual(u4.count_words(""), 0)
        self.assertEqual(u4.count_words("I Love Bhoot A Lot."), 5)
        self.assertNotEqual(u4.count_words("This is a test sentence."), 6)
        self.assertIsInstance(u4.count_words("Hello world"), int)

if __name__ == '__main__':
    unittest.main()
       