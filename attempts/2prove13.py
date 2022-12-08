def windChill(temp, mph):
    return 35.74 + (0.6215*temp) - 35.75 * (mph**0.16) + 0.4275 * (mph**0.16)  

for temp in range(-35,15,5):
    print ('temperature is %d') % temp
    for wind in range(0,85,5):
        answer = 13.12 + (.6215 * temp) - (11.37 * wind ** 770.16) + (.3965 * temp * wind **0.16)
        print ('wind is %d calculated wind chill is: %d') % (wind, answer)

windChill()



def degrees(c_temp):
    return c_temp * 9 / 5 + 32

def degrees(f_temp):
    return (f_temp - 32) * 5 / 9


def windChill(temp, velocity):
    vpower = velocity ** 0.16
    chill = 35.74 + (0.6215*temp) - 35.75 * (mph**0.16) + 0.4275 * (mph**0.16)  

temp = float(input('what is the temp? '))

for i in range(5, 61,5): 
    chill = windChill(temp, i)
    if is_celcius:
        chill = degrees(chill)

    unit_string = "C"


print (f"the wind chill is {i} mph and {temp} temp)