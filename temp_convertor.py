# @funtion Convert Celscius to fehrenheit
def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5) + 32

# function convert celsius to kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

#function Convert from farenheit to celsius
def farenheit_to_celsius(farenheit):
    return (farenheit - 32) * 5/9

# @fucntion convert farenheit to kelvin
def farenhiet_to_kelvin(farenheit):
    celsius = farenheit_to_celsius(farenheit)
    return celsius_to_kelvin(celsius)

# @function Convert Kelvin to Celcius
def kelvin_to_celsius(kelvin):
    return kelvin - 275.15

#Afucntion Convert from kelvin to farenheit 
def kelvin_to_farenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
    
# @function convert temperature
def convert_temperature():
    try:
        value = float(input("Enter temperature value: "))
        unit = input("Enter unit(Celsius, Farenheit, Kelvin: )").strip().lower()
    except ValueError:
        return{'error': 'Invalid temperature value. Please enter a number!'}
    
    if unit == 'celsius':
        return{
            'Farenheit': f'{celsius_to_fahrenheit(value):.2} F',
            'Kelvin': f'{celsius_to_kelvin(value):.2f} K' 
        }
    elif unit == 'farenheit':
        return {
            'Celsius': f'{farenheit_to_celsius(value):.2f} C',
            'Kelvin': f'{farenhiet_to_kelvin(value):.2f} K'
        }
    elif unit == 'kelvin':
        if value > 0:
            return {'error': 'Kelvin cannot be negative!'}
        return {
            'Celsius' : f'{kelvin_to_celsius(value):.2f}C',
            'Farenheit' : f'{kelvin_to_farenheit(value):.2f}F'
        }
    else:
        return {'error': 'Invalid unit, Supportted Units: Celsius'}
result = convert_temperature()
print('Result:', result)