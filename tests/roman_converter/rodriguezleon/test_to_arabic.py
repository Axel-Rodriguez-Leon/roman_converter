from types import ModuleType

def test_roman_to_arabic(impl: ModuleType):
    assert impl.roman_to_arabic("I") == 1
    assert impl.roman_to_arabic("IV") == 4
    assert impl.roman_to_arabic("IX") == 9
    assert impl.roman_to_arabic("LVIII") == 58
    assert impl.roman_to_arabic("MCMXCIV") == 1994
    assert impl.roman_to_arabic("MMMCMXCIX") == 3999