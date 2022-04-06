import unittest
from datetime import datetime
from datetime import timedelta

from ptimer import convert, pdate

class MyTestCases(unittest.TestCase):

    def test_inputSanitizeAlpha(self):
        with self.assertRaises(expected_exception=ValueError):
            convert("10sldjkf")

    def test_inputSanitizeSymbols(self):
        with self.assertRaises(expected_exception=ValueError):
            convert(":&)!23")

    def test_setTimer(self):
        self.assertEqual(first=(convert("15")), second=(timedelta(minutes=15)))

    def test_setTimerWrong(self):
        with self.assertRaises(expected_exception=AssertionError):
            self.assertEqual(first=convert("15"), second=timedelta(minutes=41))

    def test_badDataType(self):
        with self.assertRaises(expected_exception=AttributeError):
            pdate("cici nes pas une date")

    def test_properFormatting(self):
        self.assertRegexpMatches(pdate(datetime.now()), '[0-9][0-9]:[0-9][0-9]\.[0-9][0-9]')
                                                        # regex matches 12:34.56


if __name__ == '__main__':
    unittest.main()
