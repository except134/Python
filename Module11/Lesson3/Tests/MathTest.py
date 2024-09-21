import unittest
import pathlib
import sys
from unittest import runner

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

from Core.Math import *

class Test_Vector2(unittest.TestCase):
    def test_Add(self):
        vec1 = Vector2(1, 1)
        vec2 = Vector2(2, 2)
        self.assertEqual(vec1 + vec2, Vector2(3, 3))

    def test_Sub(self):
        vec1 = Vector2(2, 2)
        vec2 = Vector2(1, 1)
        self.assertEqual(vec1 - vec2, Vector2(1, 1))

    def test_Div(self):
        vec1 = Vector2([4, 4])
        self.assertEqual(vec1 / 2, Vector2(2, 2))

    def test_Mul(self):
        vec1 = Vector2([2, 2])
        self.assertEqual(vec1 * 2, Vector2(4, 4))

    def test_MidPoint(self):
        vec1 = Vector2([4, 4])
        vec2 = Vector2([2, 2])
        self.assertEqual(vec1.midPoint(vec2), Vector2(3, 3))

    def test_Dot(self):
        vec1 = Vector2([2, 2])
        vec2 = Vector2([2, 2])
        self.assertEqual(Vector2.dot(vec1, vec2), 8)

class Test_Vector3(unittest.TestCase):
    def test_Add(self):
        vec1 = Vector3(1, 1, 2)
        vec2 = Vector3(2, 2, 3)
        self.assertEqual(vec1 + vec2, Vector3(3, 3, 5))

    def test_Sub(self):
        vec1 = Vector3(2, 2, 4)
        vec2 = Vector3(1, 1, 2)
        self.assertEqual(vec1 - vec2, Vector3(1, 1, 2))

    def test_Div(self):
        vec1 = Vector3([4, 4, 4])
        self.assertEqual(vec1 / 2, Vector3(2, 2, 2))

    def test_Mul(self):
        vec1 = Vector3([2, 2, 2])
        self.assertEqual(vec1 * 2, Vector3(4, 4, 4))

    def test_MidPoint(self):
        vec1 = Vector3([4, 4, 4])
        vec2 = Vector3([2, 2, 2])
        self.assertEqual(vec1.midPoint(vec2), Vector3(3, 3, 3))

    def test_Dot(self):
        vec1 = Vector3([2, 2, 2])
        vec2 = Vector3([2, 2, 2])
        self.assertEqual(Vector3.dot(vec1, vec2), 12)

class Test_Vector4(unittest.TestCase):
    def test_Add(self):
        vec1 = Vector4(1, 1, 2, 2)
        vec2 = Vector4(2, 2, 3, 3)
        self.assertEqual(vec1 + vec2, Vector4(3, 3, 5, 5))

    def test_Sub(self):
        vec1 = Vector4(2, 2, 4, 4)
        vec2 = Vector4(1, 1, 2, 2)
        self.assertEqual(vec1 - vec2, Vector4(1, 1, 2, 2))

    def test_Div(self):
        vec1 = Vector4([4, 4, 4, 6])
        self.assertEqual(vec1 / 2, Vector4(2, 2, 2, 3))

    def test_Mul(self):
        vec1 = Vector4([2, 2, 2, 6])
        self.assertEqual(vec1 * 2, Vector4(4, 4, 4, 12))

    def test_Dot(self):
        vec1 = Vector4([2, 2, 2, 6])
        vec2 = Vector4([2, 2, 2, 6])
        self.assertEqual(Vector4.dot(vec1, vec2), 48)

MathST = unittest.TestSuite()
MathST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Vector2))
MathST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Vector3))
MathST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Vector4))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(MathST)

