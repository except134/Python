import unittest
from runner import *

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner("Walker")
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        r1 = Runner("R1")
        r2 = Runner("R2")
        for _ in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)

if __name__ == '__main__':
    unittest.main()
