# -*- coding: utf-8 -*-

import numpy as np
np.version.full_version

#%% Vector multiplication

# Multiply two one-dimensional array's
# Vector a and b need to be of the same size

a = [1, 2, 3]
b = [5, 10, 15]
ans=np.dot(a,b)


# Vector and matrix multiplication into matrix
c = [1, 2]
d = [[5, 10], [15, 20]]
np.dot(c, d)

#%% MATRIX MULTIPLICATION 

# Matrix and vector multiplication into matrix
a = [[5, 10], [15, 20]]
b = [1, 2]

# 5*1 + 10*2, 15*1 + 20*2
np.dot(a, b)

# Matrix to matrix multiplication
a = [[5, 10], [15, 20], [25, 30]]
b = [[1, 2], [3,4]]
#  5*1 + 10*3,  5*2 + 10*4
# 15*1 + 20*3, 15*2 + 20*4
# 25*1 + 30*3, 25*2 + 30*4
np.dot(a, b)

# Matrix to matrix multiplication
a = [[1, 2, 3], [4, 5, 6]]
b = [[5, 10], [15, 20], [25, 30]]

#  1*5 + 2*15 + 3*25, 1*10 + 2*20 + 3*30
#  4*5 + 5*15 + 6*25, 4*10 + 5*20 + 6*30
np.dot(a, b)
