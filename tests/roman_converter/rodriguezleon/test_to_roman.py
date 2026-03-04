from types import ModuleType

def test_arabic_to_roman(impl: ModuleType):
    assert impl.arabic_to_roman(1) == "I"
    assert impl.arabic_to_roman(4) == "IV"
    assert impl.arabic_to_roman(9) == "IX"
    assert impl.arabic_to_roman(58) == "LVIII"
    assert impl.arabic_to_roman(1994) == "MCMXCIV"
    assert impl.arabic_to_roman(3999) == "MMMCMXCIX"