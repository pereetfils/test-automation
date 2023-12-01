import pytest

from src.services.string_service import to_uppercase

@pytest.mark.skip()
def test_uppercase_with_lowercased_str():
    assert to_uppercase('hello r2-d2') == 'HELLO R2-D2'

def test_uppercase_with_uppercased_str():
    assert to_uppercase('HI YOU R2D2') == 'HI YOU R2D2'

@pytest.mark.skip
def test_uppercase_with_no_str():
    assert to_uppercase('') == ''

@pytest.mark.skip
def test_uppercase_with_not_str():
    assert to_uppercase(2) == 2
