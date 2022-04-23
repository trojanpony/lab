import unittest

from numpy import power
from classes import Television

class MyTest(unittest.TestCase):
    tv = Television()
    def test_power(tv):
        tv.power()
        assert tv.status == True
        tv.power()
        assert tv.status == False
    def main():
        test_power()


if __name__ == '__main__':
    MyTest.main()