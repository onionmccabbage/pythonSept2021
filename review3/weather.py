from random import randint
from countries import countries

class Weather():
    '''
    The Weather class takes a non-empty string for the description
    and a floating point number for the temperature
    '''
    def __init__(self, city, country, desc, temp):
        self.city = city
        self.country = country
        self.desc = desc # make use of the setter methods
        self.temp = temp
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new_city):
        # must be a string of 2 or more characters
        if type(new_city) == str and len(new_city) >1:
            self.__city = new_city
        else:
            self.__city = 'Athlone' # default
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, new_country):
        # must be a string that matches the permitted values
        if type(new_country) == str and new_country in countries:
            self.__country = new_country
        else:
            self.__country = 'ie' # default
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, new_desc):
        # must be a non-empty string
        if type(new_desc) == str and new_desc != '':
            self.__desc = new_desc
        else:
            self.__desc = 'fine' # default
    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self, new_temp):
        # must be numeric
        if type(new_temp) == int or type(new_temp) == float:
            self.__temp = new_temp
        else:
            self.__temp = 12 # a reasonable default
    def tempInKelvin(self):
        # alter the temperature by a small random amount
        tempK = self.temp + 273
        return tempK # this is a derived property - does not persist
    def __makeInitialCaps(self, prop):
        return prop.title()
    def __str__(self):
        # output a nicely formatted weather report
        ci = self.__makeInitialCaps(self.city)
        co = self.__makeInitialCaps(self.country)
        d = self.__makeInitialCaps(self.desc)
        report  = 'The weather in {3}, {4} is {0} at {1:.2f}C ({2:.2f}K)'.format(d, self.__temp, self.tempInKelvin(), ci, co)
        return report

if __name__ == '__main__':
    # exercise this module
    w_ath = Weather('athlone', 'ie', 'rainy', 9.04)
    w_gal = Weather('galway', 'ie', 'windy', 6.70)
    w_kt = Weather('kinston', 'jm', 'Sunny', 27.98)
    print(w_gal.tempInKelvin()) # NB does NOT use the __str__ method since we are not printing the whole class
   
    print(w_ath)
    print(w_gal)
    print(w_kt)

    w_default = Weather(True, 999, [], ()) # wrong data types so should fall back to the defaults
    print(w_default)
