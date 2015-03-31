'''
Created on Mar 31, 2015

@author: pd878
'''
if __name__ == "__main__":
    pass

import numpy as np 
import matplotlib.pyplot as plt

########################
#       Task 1         #
########################

print '\nStarting Task 1...\n'
#constructs the array
x = np.arange(1,16,1)
y = x.reshape(3, 5)
z = y.transpose()

a = z[(1,3),:]
print "\nTask 1a result:\n", a

b = z[:,1]
print "\nTask 1b result:\n", b

c = z[1:4,0:3]    #includes the coordicates
print "\nTask 1c result:\n", c

d = z[np.logical_and(z>3, z<11)]
print "\nTask 1d result:\n", d


########################
#       Task 2         #
########################

print '\nStarting Task 2...\n'

a = np.arange(25).reshape(5, 5)
b = np.array([1., 5, 10, 15, 20])

c = b.reshape(5, 1)
result = a/c
print 'Task 2 result:\n', result

########################
#       Task 3         #
########################

print '\nStarting Task 3...\n'

x = np.random.rand(10, 3)

diff = np.abs(x-0.5)
a = diff.min(axis = 1)

b = np.argsort(diff, axis = 1)[:,0]

row_array = np.arange(10)
c = x[row_array, b]
print '\nTask 3 result:\n',c


########################
#       Task 4         #
########################

print '\nStarting Task 4...\n'

#computation parameter setting
N_max = 50  #Number of iteration
some_threshold = 50
pixel_x = 1000j
pixel_y = 1000j

#Constructing a grid of c = x + 1j*y values in the range [-2, 1]*[-1.5, 1.5]
x,y=np.ogrid[-2:1:pixel_x,-1.5:1.5:pixel_y]

c=x + 1j*y
z=c

print '\nStarting %d iteration...\n' %(N_max)

#starts iteration
for v in range(N_max):
        #print 'Iteration number: ', v
        z=z**2 + c

mask = np.abs(z) < some_threshold

print '\nPlotting using imshow()\n' 
plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])
plt.gray()

print '\nSaving figure as mandelbrot.png\n'
plt.savefig('mandelbrot.png')







    
    