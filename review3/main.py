from weather import Weather

def main():
    '''
    invoke the Weather class to create instances of weather reports
    '''
    w_edi = Weather('Belfast', 'uk', 'rainy', -3.7)
    w_gal = Weather('Athlone', 'ie', 'humid', 5)
    w_kt = Weather('Kingston', 'jm', 'sunny', 32)
    w_default = Weather('Utopia', '', '__', True)
    # lets see the instances
    print(w_edi)
    print(w_gal)
    print(w_kt)
    print(w_default)
    # ask the user for some details
    city = input('Which city? ')
    country = input('Which country? ')
    desc = input('Weather Description? ')
    temperature = input('Temperature? ')
    u = Weather(city, country, desc, temperature)
    print(u)

if __name__ == '__main__':
    main()

