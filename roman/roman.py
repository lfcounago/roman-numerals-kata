def roman_encoder(decimal: int) -> str:
    """Translates from decimal to Roman Numeral string"""

    roman = int(decimal/1000) * "M"
    decimal = decimal - int(decimal/1000)*1000
    
    roman = roman + int(decimal/900) * "CM"
    decimal = decimal - int(decimal/900)*900
    
    roman = roman + int(decimal/500) * "D"
    decimal = decimal - int(decimal/500)*500
    
    roman = roman + int(decimal/400) * "CD"
    decimal = decimal - int(decimal/400)*400
    
    roman = roman + int(decimal/100) * "C"
    decimal = decimal - int(decimal/100)*100
    
    roman = roman + int(decimal/90) * "XC"
    decimal = decimal - int(decimal/90)*90
    
    roman = roman + int(decimal/50) * "L"
    decimal = decimal - int(decimal/50)*50
    
    roman = roman + int(decimal/40) * "XL"
    decimal = decimal - int(decimal/40)*40
    
    roman = roman + int(decimal/10) * "X"
    decimal = decimal - int(decimal/10)*10
    
    roman = roman + int(decimal/9) * "IX"
    decimal = decimal - int(decimal/9)*9
    
    roman = roman + int(decimal/5) * "V"
    decimal = decimal - int(decimal/5)*5
    
    roman = roman + int(decimal/4) * "IV"
    decimal = decimal - int(decimal/4)*4
    
    roman = roman + decimal * "I"
    
    return roman


def roman_decoder(roman: str) -> int:
    """Translates from Roman Numeral string to decimal"""
    pass