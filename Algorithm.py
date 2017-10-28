import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)

x = np.array([1, 4, 5, 10])
y = np.array([1, 7, 5,  8])

plt.plot(x[ : : 2], y[ : : 2], linestyle = '--', color = 'black')
plt.plot(x[2  :  ], y[2  :  ], linestyle = '--', color = 'black')
plt.plot(x[:  : 3], y[ : : 3],  linestyle = '--', color = 'red')
plt.scatter(x, y, c = 'black', zorder = 99)
plt.scatter([5, 8], [2, 3], c = 'black', zorder = 99)
plt.scatter([6], [4.9], c = 'red')
plt.title('EDPath Routing Algorithm')
#plt.xlabel('x [-]')
#plt.ylabel('y [-]')
plt.annotate('Optimal\nendpoint', xy = (6.2, 4.8), xytext = (7.5, 4),
             arrowprops = dict(facecolor = 'black', arrowstyle = "->",
             connectionstyle = "arc3"))

plt.annotate('Nearest star', xy = (4.8, 5), xytext = (2, 6),
             arrowprops =dict(facecolor = 'black', arrowstyle = "->",
             connectionstyle = "arc3"))

plt.annotate('Start', xy = (1, 1.2), xytext = (1, 3),
             arrowprops=dict(facecolor = 'black', arrowstyle = "->",
             connectionstyle = "arc3"))

plt.annotate('Target', xy = (10, 7.8), xytext = (9, 5),
             arrowprops=dict(facecolor = 'black', arrowstyle = "->",
             connectionstyle = "arc3"))

plt.annotate('', xy = (1.2, 0.9), xytext = (6.3, 4.7),
             arrowprops=dict(facecolor = 'black', arrowstyle = "<->",
             connectionstyle = "arc3"))

plt.text(3.8, 3.1, 'Jump range', rotation = 35)
plt.axis('off')
plt.savefig('EDPath.png')
plt.savefig('EDPath.pdf')

plt.rcParams['figure.figsize'] = (6, 4)