import matplotlib.pyplot as plt
import numpy as np
import serial
import time

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)

t = np.arange(0,10,0.1) 
X = np.arange(0,10,0.1)
Y = np.arange(0,10,0.1)
Z = np.arange(0,10,0.1)
MOVES = np.arange(0,10,0.1)

for x in range(0,100):
    line=s.readline()
    X[x] = float(line)
    line=s.readline()
    Y[x] = float(line)
    line=s.readline()
    Z[x] = float(line)
    line=s.readline()
    MOVES[x] = float(line)

fig, ax = plt.subplots(2, 1)
ax[0].plot(t,X,color = 'blue',linestyle = '-',label = 'x')
ax[0].plot(t,Y,color = 'red',linestyle = '-',label = 'y')
ax[0].plot(t,Z,color = 'green',linestyle = '-',label = 'z')
ax[0].legend(loc = 'lower left')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].plot(t,MOVES)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('MOVES')
plt.show()
s.close()