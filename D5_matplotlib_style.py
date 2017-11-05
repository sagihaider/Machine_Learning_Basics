# -*- coding: utf-8 -*-

#matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create 500 evenly spaced numbers from 0 to 10
# Showing the last 20 values
x = np.linspace(0, 10, 500)
x[1:10]

# Get the available styles
print(plt.style.available)

plt.title('Default MatPlotLib')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, np.log(x))
plt.show()

# Plot the default Baysian Methods for Hackers style
plt.style.use('bmh')
plt.title('Baysian Methods for Hackers')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, x**8)
plt.show()

# Plot the GGPlot like style
plt.style.use('ggplot')
plt.title('GGPlot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, x**8)
plt.show()

plt.style.use('grayscale')
plt.title('Grayscale')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, x**8)
plt.show()




plt.style.use('fivethirtyeight')
plt.title('Nate Silver fivethirtyeight.com')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, x**8)
plt.show()




plt.style.use('dark_background')
plt.title('Dark Background')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, x**8)
plt.show()