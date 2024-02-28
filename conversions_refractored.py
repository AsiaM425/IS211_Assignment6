class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    if fromUnit == "Celsius" and toUnit == "Kelvin":
        return value + 273.15
    elif fromUnit == "Celsius" and toUnit == "Fahrenheit":
        return (value * 9/5) + 32
    elif fromUnit == "Fahrenheit" and toUnit == "Celsius":
        return (value - 32) * 5/9
    elif fromUnit == "Fahrenheit" and toUnit == "Kelvin":
        return (value + 459.67) * 5/9
    elif fromUnit == "Kelvin" and toUnit == "Celsius":
        return value - 273.15
    elif fromUnit == "Kelvin" and toUnit == "Fahrenheit":
        return (value * 9/5) - 459.67
    elif fromUnit == toUnit:
        return value
    else:
        raise ConversionNotPossible("Conversion from {} to {} is not possible".format(fromUnit, toUnit))

