v = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60] 

def wind_chill(t, v):
    v_power = v ** 0.16
    wind = 35.74 + (0.6215*t) - 35.75 * (v**0.16) + 0.4275 * (v**0.16)  
    return wind

def c_to_f(temp):
    t = (temp * (9/5)) + 32
    return t

temp = int(input("What is the temperature? "))
degrees = input("Fahrenheit or Celsius (f/c)? ").upper()

if degrees == "F":
    for value in v:
        t = temp
        chill = wind_chill(t, value)
        print (f"At temperature {t:.1f}F, and wind speed {value} mph, the windchill is: {chill:.2f}F" )
elif degrees == "C":
    for value in v:
        t = c_to_f(temp)
        chill = wind_chill(t, value)
        print (f"At temperature {t:.1f}F, and wind speed {value} mph, the windchill is: {chill:.2f}F" )
