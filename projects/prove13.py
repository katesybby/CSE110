print ('\nWIND SPEED CALCULATOR')

playing = "y"
while playing == "y":
    windspeeds = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60] 

    def wind_chill(t, v):
        wind = 35.74 + (0.6215*t) - (35.75 * (v**.16)) + ((t*.4275) * (v**.16))  
        return wind

    def c_to_f(t, f_or_c, v):
        if f_or_c == "F" or "f":
                wind = wind_chill(t, v)
                return wind

        elif f_or_c == "C" or "c":
            t = (t * (9/5)) + 32
            wind = wind_chill(t, v)
            return wind

    t = int(input('\nWhat is the temperature? '))
    f_or_c = input('Fahrenheit or Celsius (F/C)? ')

    for v in windspeeds:
        result = c_to_f(t, f_or_c, v)
        print (f"At temperature {t:.1f}F, and wind speed {v} mph, the windchill is: {result:.2f}F" )

    playing = input('\nDo you want to test another temperature (y/n)? ')

    if playing == 'n':
        print ('Goodbye')