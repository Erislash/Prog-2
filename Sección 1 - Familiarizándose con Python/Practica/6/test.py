import pytest
from main import *


def testFirstNumbers():
    assert sumFirstN(-4, 0) == -6
    assert sumFirstN(0, 4) == 6
    assert sumFirstN(0, 10) == 45
    assert sumFirstN(0, 0) == 0
    assert sumFirstN(2, 4) == 3

def runTests():
    testFirstNumbers()

runTests()