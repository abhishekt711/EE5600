import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2, 2, 100)

 
y = x**2 -  1 
a = 1
b =0
c =-1

d1 = -b + np.sqrt(b**2-4*a*c)
d2 = -b - np.sqrt(b**2-4*a*c)
d1 = d1/(2*a)
d2 = d2/(2*a)

print("The solutions of the equations are",d1,"and",d2)




fig, ax = plt.subplots()
ax.plot(x, y)
plt.grid()

plt.plot(d2,0, 'o')
plt.text(d2,0.5, 'D')
plt.plot(d1, 0, 'o')
plt.text(d1,0.5, 'E')



plt.xlabel('$x$');plt.ylabel('$y$')

plt.show()
