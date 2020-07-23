import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpu6050 import mpu6050
import datetime as dt


fig, ax = plt.subplots()
mpu = mpu6050(0x68)
frame = []
x = []
y = []
z = []
plotx, = ax.plot(frame, x, color = 'r', label ='x')
ploty, = ax.plot(frame, y, color = 'g', label ='y')
plotz, = ax.plot(frame, z, color = 'b', label ='z')
# Parameters
x_len = 200         # Number of points to display
y_range = [10, 40]  # Range of possible Y values to display

def animate(i, x, y, z):
    data = mpu.get_accel_data()
    frame.append(dt.datetime.now().strftime('%H:%M:%S'))
    x.append(data['x'])
    y.append(data['y'])
    z.append(data['z'])
    #ax.plot(frame, x, label='Channel x')
    #ax.plot(frame, y, label='Channel y')
    #ax.plot(frame, z, label='Channel z')
    plotx.set_data(x)
    ploty.set_data(y)
    plotz.set_data(z)
    plt.legend(loc='upper left')
    plt.title('esta puede ser eh')
    plt.ylabel('m/s2')
    return plotx, ploty, plotz


# levanto y grafico con animate
ani = FuncAnimation(fig, animate, fargs=(x, y, z,), interval=50, blit=True)
plt.tight_layout()
ani.save('medicion.gif', writer="imagemagick")
fig.savefig('medicion_last_frame.png')
plt.show()
