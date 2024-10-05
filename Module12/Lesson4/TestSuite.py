import unittest
import runner_and_tournament_test as tester 

suite = unittest.TestSuite()

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tester.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)


