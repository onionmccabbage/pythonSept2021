from countries import countries
from weather import Weather

class LocalWeather(Weather): # inherit from our Weather class
    def __init__(self, city='Athlone', country='ie', desc='fine', temp=12): # sensible default for country
        super().__init__(desc, temp) # we call the parent class constructor
        self.city = city
        self.country = country # use the setter method
    def __str__(self):
        loc = 'Local weather in {}, {} is {} at {:.2f}C'.format(self.__city, self.country, self.desc, self.temp)
        return loc
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new_city):
        if type(new_city) == str and new_city != '':
            self.__city = new_city
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, new_country):
        if type(new_country) == str and new_country !='' and new_country in countries:
            self.__country = new_country
        else:
            self.__country = 'uk' # default
if __name__ == '__main__':
    l1 = LocalWeather('Edinburgh', 'uk', 'rainy', -3.7)
    l2 = LocalWeather('Galway', 'ie', 'humid', 5)
    l3 = LocalWeather('Kingston', 'jm', 'sunny', 32)
    l4 = LocalWeather('Begonia', 'es', True ,True)
    print('{}\n{}\n{}\n{}\n'.format(l1, l2, l3, l4))
