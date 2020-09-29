#Упражнение №2
'''Постройте график функции y(x) = x*x - x - 6
и по графику найдите найдите корни уравнения y(x) = 0.
(Не нужно применять численных методов — просто приблизьте график к корням
 функции настолько, чтобы было удобно их найти.)'''
import numpy as np
import matplotlib.pyplot as diagram

x= np.arange(-100,+100,0.1)
y= x*x - x - 6
diagram.xlabel('X')
diagram.ylabel('Y(X)')
diagram.grid('True')
diagram.plot(x,y)
diagram.show()

# Корни уравнения y(x) = 0 (x=-2,0 y=3,0)

