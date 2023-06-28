from roman.roman import roman_encoder


def test_encoder_1000_should_return_M():
    expected = "M"
    actual = roman_encoder(1000)
    assert expected == actual

def test_encoder_2000_should_return_MM():
    expected = "MM"
    actual = roman_encoder(2000)
    assert expected == actual

def test_encoder_3000_should_return_MMM():
    expected = "MMM"
    actual = roman_encoder(3000)
    assert expected == actual

def test_encoder_500_should_return_D():
    expected = "D"
    actual = roman_encoder(500)
    assert expected == actual

def test_encoder_1500_should_return_MD():
    expected = "MD"
    actual = roman_encoder(1500)
    assert expected == actual

def test_encoder_1700_should_return_MDCC():
    expected = "MDCC"
    actual = roman_encoder(1700)
    assert expected == actual

def test_encoder_1750_should_return_MDCCL():
    expected = "MDCCL"
    actual = roman_encoder(1750)
    assert expected == actual

def test_encoder_1760_should_return_MDCCLX():
    expected = "MDCCLX"
    actual = roman_encoder(1760)
    assert expected == actual

def test_encoder_1765_should_return_MDCCLXV():
    expected = "MDCCLXV"
    actual = roman_encoder(1765)
    assert expected == actual

def test_encoder_40_should_return_XL():
    expected = "XL"
    actual = roman_encoder(40)
    assert expected == actual

def test_encoder_140_should_return_CXL():
    expected = "CXL"
    actual = roman_encoder(140)
    assert expected == actual

def test_encoder_90_should_return_XC():
    expected = "XC"
    actual = roman_encoder(90)
    assert expected == actual

def test_encoder_900_should_return_CM():
    expected = "CM"
    actual = roman_encoder(900)
    assert expected == actual

def test_encoder_400_should_return_CD():
    expected = "CD"
    actual = roman_encoder(400)
    assert expected == actual

def test_encoder_940_should_return_CMXL():
    expected = "CMXL"
    actual = roman_encoder(940)
    assert expected == actual

def test_encoder_4_should_return_IV():
    expected = "IV"
    actual = roman_encoder(4)
    assert expected == actual

def test_encoder_9_should_return_IX():
    expected = "IX"
    actual = roman_encoder(9)
    assert expected == actual

def test_encoder_1_should_return_I():
    expected = "I"
    actual = roman_encoder(1)
    assert expected == actual

def test_encoder_2_should_return_II():
    expected = "II"
    actual = roman_encoder(2)
    assert expected == actual

def test_encoder_3_should_return_III():
    expected = "III"
    actual = roman_encoder(3)
    assert expected == actual

def test_encoder_999_should_return_CMXCIX():
    expected = "CMXCIX"
    actual = roman_encoder(999)
    assert expected == actual
    
