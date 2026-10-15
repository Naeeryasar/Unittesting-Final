import unittest
import main

class TestStringProcessor(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(main.reverse("Hello world"), "dlrow olleH")
        self.assertEqual(main.reverse("Python"), "nohtyP")
        self.assertEqual(main.reverse(""), "")
        self.assertNotEqual(main.reverse("Hello world"), "Hello world")
        self.assertIsInstance(main.reverse("Hello world"), str)

    def test_count_vowels(self):
        self.assertEqual(main.count_vowels("Hello world"), 3)
        self.assertIsInstance(main.count_vowels("Hello world"), int)
        self.assertRaises(TypeError, main.count_vowels, None)
        self.assertNotEqual(main.count_vowels("Python"), 3)
        self.assertEqual(main.count_vowels("This is a test sentence."), 7)
