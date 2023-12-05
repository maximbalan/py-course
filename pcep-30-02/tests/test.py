import unittest
import pytest
import pcep_30_02 as pcep


class TestValues(unittest.TestCase):

  def test_a(self):
    self.assertEqual(pcep.a, 10)

  def test_b(self):  
    self.assertEqual(pcep.b, 10)

  def test_c(self):
    self.assertEqual(pcep.c, 10)

  def test_d(self):
    self.assertEqual(pcep.d, 10)

if __name__ == '__main__':
  unittest.main()
