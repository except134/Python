import unittest
import runner_and_tournament as rat 

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    def setUp(self):
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for d in cls.all_results.values():
            new_dict = {}
            for key, value in d.items():
                new_dict[key] = value.name
            print(new_dict)
 
    def test_tournament1(self):
        tournament = rat.Tournament(90, self.runner1, self.runner3)
        self.all_results['test_tournament1'] = tournament.start()
        self.assertTrue((self.all_results.get('test_tournament1')).get(max(self.all_results.get('test_tournament1')))
                        == self.runner3.name)

    def test_tournament2(self):
        tournament = rat.Tournament(90, self.runner2, self.runner3)
        self.all_results['test_tournament2'] = tournament.start()
        self.assertTrue((self.all_results.get('test_tournament2')).get(max(self.all_results.get('test_tournament2')))
                        == self.runner3.name)

    def test_tournament3(self):
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results['test_tournament3'] = tournament.start()
        self.assertTrue((self.all_results.get('test_tournament3')).get(max(self.all_results.get('test_tournament3')))
                        == self.runner3.name)

if __name__ == '__main__':
    unittest.main()
