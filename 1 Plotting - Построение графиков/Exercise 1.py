#Пример построения графика функции:
'''import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x**2)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.00001)
plt.plot(x, x**2)
plt.show()'''

#На одном рисунке можно построить несколько графиков функций:
'''import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x*6)
plt.show()'''

#Также довольно просто на график добавить служебную информацию и отобразить сетку:
'''import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r"f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x")
plt.grid(True)
plt.show()'''

'''import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.figure(figsize=(10, 5))
plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
plt.plot(x, -x, label=r'$f_3(x)=-x$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=10)
plt.show()'''

'''import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(50,10))
x = np.arange(-10, 10.01, 0.01)
t = np.arange(-10, 11, 1)

#subplot 1
sp = plt.subplot(141)
plt.plot(x, np.sin(x))
plt.title(r'$\sin(x)$')
plt.grid(True)

#subplot 2
sp = plt.subplot(142)
plt.plot(x, np.cos(x), 'g')
plt.axis('equal')
plt.grid(True)
plt.title(r'$\cos(x)$')

#subplot 3
sp = plt.subplot(143)
plt.plot(x, x**2, t, t**2, 'ro')
plt.title(r'$x^2$')

#subplot 4
sp = plt.subplot(144)
plt.plot(x, x)
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')
plt.title(r'$x$')
plt.show()'''


#График может быть построен в полярной системе координат, для этого при создании subplot необходимо указать параметр polar=True:
'''import numpy as np
import matplotlib.pyplot as plt
plt.subplot(111, polar=True)
phi = np.arange(0, np.pi, 0.01)
rho = 2*phi/2
plt.plot(phi, rho**2, lw=1)
plt.show()'''

'''import numpy as np
import matplotlib.pyplot as plt
t = np.arange(-2*np.pi, 2*np.pi, 0.01)
r = 2
plt.plot(r*np.sin(t), r*np.cos(t)**100, lw=3)
plt.axis('equal')
plt.show()'''
#Добавление текста на график:
'''import numpy as np
import matplotlib.pyplot as plt
mu, sigma = 50, 15
x = mu + sigma * np.random.randn(10000)
# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .030, r'$\mu=100,\ \sigma=15$')
plt.text(50, .033, r'$\varphi_{\mu,\sigma^2}(x) = \frac{1}{\sigma\sqrt{2\pi}} \,e^{ -\frac{(x- \mu)^2}{2\sigma^2}} = \frac{1}{\sigma} \varphi\left(\frac{x - \mu}{\sigma}\right),\quad x\in\mathbb{R}$', fontsize=20, color='red')
plt.axis([40, 160, 0, 0.04])
plt.grid(True)
plt.show()'''