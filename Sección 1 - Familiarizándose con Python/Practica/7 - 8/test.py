import pytest
from main import *


def testMultiplyString():
    assert multiplyString('Zehnya', 3) == 'ZehnyaZehnyaZehnya'
    assert multiplyString('', 10) == ''
    assert multiplyString('ReNo', 5) == 'ReNoReNoReNoReNoReNo'

def runTests():
    print('Running Tests...')
    testMultiplyString()

    print('...all tests finished')

runTests()