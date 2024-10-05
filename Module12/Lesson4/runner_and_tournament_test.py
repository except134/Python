import unittest
import runner_and_tournament as rat 
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            walker = rat.Runner("Walker", -5)
            for _ in range(10):
                walker.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(walker.distance, 50)
        except(ValueError):
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = rat.Runner(10)
            for _ in range(10):
                runner.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(runner.distance, 100)
        except(TypeError):
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

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
