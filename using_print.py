# there are several ways to print

x = 1

# repr is hte actual representation whereas print uses a __str__() method, which can be customized
print( repr(x) ) # we almost always use print rather than repr

# we can format printed output
temperature = 12
description = 'sunny'
wind_speed = 6.7654321
#                                                   position 1:0.4f means 4 dp float
report = 'The weather is {0} (yes {0}) with a wind speed of {1:0.4f} an a temperature of {2}'
print(report.format(description, wind_speed, temperature))
