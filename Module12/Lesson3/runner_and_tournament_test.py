import unittest
import runner_and_tournament as rat 

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            d = {}
            for key, value in i.items():
                d[key] = value.name
            print(d)

    def setUp(self):
        self.runUsain = rat.Runner('Усэйн', 10)
        self.runAndrew = rat.Runner('Андрей', 9)
        self.runNick = rat.Runner('Ник', 3)
 
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        t = rat.Tournament(90, self.runUsain, self.runNick)
        res = t.start()
        self.all_results[len(self.all_results) + 1] = res
        self.assertTrue(res[max(res.keys())] == self.runNick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        t = rat.Tournament(90, self.runAndrew, self.runNick)
        res = t.start()
        self.all_results[len(self.all_results) + 1]  = res
        self.assertTrue(res[max(res.keys())] == self.runNick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        t = rat.Tournament(90, self.runUsain, self.runAndrew, self.runNick)
        res = t.start()
        self.all_results[len(self.all_results) + 1] = res
        self.assertTrue(res[max(res.keys())] == self.runNick.name)

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = rat.Runner("Walker")
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = rat.Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = rat.Runner("R1")
        r2 = rat.Runner("R2")
        for _ in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)

if __name__ == '__main__':
    unittest.main()
