#Упражнение №3
'''Постройте график функции
http://cs.mipt.ru/python/images/lab1/task3.png'''

import numpy as math
import matplotlib.pyplot as diagram

x = math.arange(-100,+100,0.01)
y =  math.log((x**2 + 1) * math.exp(- math.absolute( x ) / 10 ) ) / math.log( 1 + math.tan( 1 / 1 + math.sin( x )**2) )
diagram.xkcd()
diagram.plot( x , y )
diagram.show()