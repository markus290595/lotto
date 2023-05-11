from unittest import TestCase, TestSuite, TextTestRunner
from lotto import lottozahlen_simulator

erste = 1
letzte = 46
ziehungen = 6 
anzahl = 1000


class LottoTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.lotto = lottozahlen_simulator(
                        erste = erste,
                        letzte = letzte,
                        ziehungen = ziehungen, 
                        anzahl = anzahl
                    )
        
    def test_list_creation(self):
        self.assertTrue(
            isinstance(self.lotto._liste_lottozahlen, list),
            'Lottozahlen ist nicht als Liste definiert'
        )

    def test_return_mean(self):
        self.assertTrue(
            isinstance(self.lotto.return_mean()/1, float),
            'Mittelwert ist keine Zahl'
        )

    def test_amount_check(self):
        self.assertEqual(
            len(self.lotto._liste_lottozahlen),
            self.lotto._anzahl,
            'Anzahl der Lottospiele ungleich der gewünschten Anzahl'
        )

def suite():
    test_suite = TestSuite()

    test_suite.addTest(LottoTest('test_list_creation'))
    test_suite.addTest(LottoTest('test_return_mean'))
    test_suite.addTest(LottoTest('test_amount_check'))

    return test_suite

if __name__ == '__main__':
    runner = TextTestRunner()
    test_result = runner.run(suite())

    number_of_err = len(test_result.errors)
    number_of_fail = len(test_result.failures)
    number_of_tests = test_result.testsRun

    print(number_of_err, number_of_fail, number_of_tests)