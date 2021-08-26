import pytest
from main import *


def testFirstNumbers():
    assert sumFirstN(10) == 55
    assert sumFirstN(3) == 6
    assert sumFirstN(0) == 0
    assert sumFirstN(2) == 3
    assert sumFirstN(122) == 7503
    assert sumFirstN(44) == 990

def runTests():
    testFirstNumbers()

runTests()