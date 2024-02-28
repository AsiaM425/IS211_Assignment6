import conversions

def test_convertCelsiusToKelvin():
    test_cases = [(0, 273.15), (100, 373.15), (-40, 233.15), (25, 298.15), (50, 323.15)]
    for celsius, expected_kelvin in test_cases:
        result = conversions.convertCelsiusToKelvin(celsius)
        assert result == expected_kelvin, f"Expected {expected_kelvin} K for {celsius}°C, but got {result} K"

def test_convertCelsiusToFahrenheit():
    test_cases = [(0, 32), (100, 212), (-40, -40), (25, 77), (50, 122)]
    for celsius, expected_fahrenheit in test_cases:
        result = conversions.convertCelsiusToFahrenheit(celsius)
        assert result == expected_fahrenheit, f"Expected {expected_fahrenheit}°F for {celsius}°C, but got {result}°F"

if __name__ == "__main__":
    test_convertCelsiusToKelvin()
    test_convertCelsiusToFahrenheit()
    print("All tests passed!")

