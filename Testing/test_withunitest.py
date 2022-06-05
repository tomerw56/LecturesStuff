import unittest
from Example_Demo.MyCrazyCalculator import myCrazyCalclulator


class TestSimpleWithUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.example = 0
        print("this is called at the beginning of the class")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.example = 0
        print("this is called at the end of the class")

    def setUp(self) -> None:
        print("this is called before every test")
        self.example += 1
        print(f"value of example {self.example}")

    def tearDown(self) -> None:
        print("this is called after every test")
        self.example += 1
        print(f"value of example {self.example}")

    def test_add_not_crazy(self):
        calculator = myCrazyCalclulator()
        self.assertTrue(calculator.add(1, 3) == 4)
        self.assertEqual(calculator.add(1, 3), 4)

    def test_muinus_not_crazy(self):
        calculator = myCrazyCalclulator()
        self.assertEqual(calculator.add(1, 0), 1)
