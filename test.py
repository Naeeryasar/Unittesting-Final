import unittest
import main

class TestStringProcessor(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(main.reverse("Hello world"), "dlrow olleH")
        self.assertEqual(main.reverse("Python"), "nohtyP")
        self.assertEqual(main.reverse(""), "")
        self.assertNotEqual(main.reverse("Hello world"), "Hello world")
        self.assertIsInstance(main.reverse("Hello world"), str)

    
