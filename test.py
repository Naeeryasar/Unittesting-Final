import unittest
import u4

class TestStringProcessor(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(u4.reverse("Hello world"), "dlrow olleH")
        self.assertEqual(u4.reverse("Python"), "nohtyP")
        self.assertEqual(u4.reverse(""), "")
        self.assertNotEqual(u4.reverse("Hello world"), "Hello world")
        self.assertIsInstance(u4.reverse("Hello world"), str)


if __name__ == '__main__':
    unittest.main()
       