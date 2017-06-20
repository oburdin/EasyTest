import pytest

def summarize(a, b):
    return a+b


def test_easy_start_2x2():
    assert summarize(2, 2) == 4


def test_easy_start_2x2_fail():
    assert summarize(2, 2) == 5


def test_easy_start_fail():
    assert summarize('a', None)


def test_easy_start_2p3():
    a = 3
    b = 2

    assert summarize(a, b) == 6
