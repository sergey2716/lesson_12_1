
import unittest

from main_12_1 import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = Runner('Nik')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance,50)

    def test_run(self):
        runner_2 = Runner('Max')
        for i in range(10):
            runner_2.run_()
        self.assertEqual(runner_2.distance,100)

    def test_challenge(self):
        runner_3 = Runner('olga')
        runner_4 = Runner('Anton')
        for i in range(10):
            runner_3.run_()
        for i in range(10):
            runner_4.walk()
        self.assertNotEqual(runner_3.distance,runner_4.distance)

if __name__ == '__main__':
    unittest.main()
