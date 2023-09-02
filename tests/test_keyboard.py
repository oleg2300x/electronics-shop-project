
from src.keyboard import Keyboard, MixinLanguage

import pytest

def test_init_mix():
    mix = MixinLanguage()
    assert mix.language == 'EN'

def test_change_lang():
    mix1 = MixinLanguage()
    mix1.change_lang()
    assert mix1.language == 'RU'
    mix1.change_lang()
    assert mix1.language == 'EN'

def test_language():
    mix2 = MixinLanguage()
    mix2.language = 'EN'
    assert mix2.language == 'EN'
    mix2.language = 'RU'
    assert mix2.language == 'RU'

def test_invalid_keyboard():
    mixinvalidkb = MixinLanguage()
    with pytest.raises(AttributeError):
        mixinvalidkb.language = 'TR'



def test_keyboard_init():
    keybord = Keyboard('Hiper 2000', 100000, 4)
    assert keybord.name == 'Hiper 2000'
    assert keybord.price == 100000
    assert keybord.quantity == 4
