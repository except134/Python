import unittest
import runner_and_tournament as rat 

class TournamentTest(unittest.TestCase):
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
 
    def test_tournament1(self):
        t = rat.Tournament(90, self.runUsain, self.runNick)
        res = t.start()
        self.all_results[len(self.all_results) + 1] = res
        self.assertTrue(res[max(res.keys())] == self.runNick.name)

    def test_tournament2(self):
        t = rat.Tournament(90, self.runAndrew, self.runNick)
        res = t.start()
        self.all_results[len(self.all_results) + 1]  = res
        self.assertTrue(res[max(res.keys())] == self.runNick.name)

    def test_tournament3(self):
        t = rat.Tournament(90, self.runUsain, self.runAndrew, self.runNick)
        res = t.start()
        self.all_results[len(self.all_results) + 1] = res
        self.assertTrue(res[max(res.keys())] == self.runNick.name)

if __name__ == '__main__':
    unittest.main()
