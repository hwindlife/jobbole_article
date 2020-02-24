import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for i in range(1, 2):
            for j in range(1, 2):
                self.assertEqual(i + j, 1, "wrong")


if __name__ == '__main__':
    unittest.main()

