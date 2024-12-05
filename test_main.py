import unittest
import main

class TestMain(unittest.TestCase):
  def test_add(self):
    self.assertEqual(main.add(2, 3), 5)
    self.assertEqual(main.add(-1, 1), 0)

  def test_subtract(self):
    self.assertEqual(main.subtract(5, 2), 3)
    self.assertEqual(main.subtract(1, 1), 0)

if __name__ == '__main__':
  unittest.main()