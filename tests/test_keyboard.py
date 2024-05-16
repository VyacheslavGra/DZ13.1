import pytest

from src.keyboard import Keyboard

item5 = Keyboard("питон", 10000, 20, 2)

def test_language():
    assert item5.language == 'EN'

def test_change_lang():
    item5.change_lang()
    assert item5.language == 'RU'
