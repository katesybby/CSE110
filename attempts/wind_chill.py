def calculate_windchill_fah(t, v):
    wind_chill_fah = 35.74 + (0.6215 * t) - 35.75(v ** 0.16) + ((t * 0.4275) * (v ** 0.16))
    return wind_chill_fah

def convert_cel(t, fah_or_cel, v):
    if fah_or_cel == "f":
        wind_chill_fah = calculate_windchill_fah(t, v)
        return wind_chill_fah

    elif fah_or_cel == "c":
        t = (t * (9/5)) + 32
        wind_chill_fah = calculate_windchill_fah(t, v)
        wind_chill_cel = wind_chill_fah
        return wind_chill_cel

windspeeds = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
t = int(input('What is the tempurature? '))
fah_or_cel = input('Fahrenheit or Celcius (F/C)? ')

for v in windspeeds:
    result = convert_cel(t, fah_or_cel, v)
    print(f'At tempurature {t}F, and wind speed {v} mph, the wind chill is: {result:.2f}F')