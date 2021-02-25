#https://matplotlib.org/3.3.3/users/event_handling.html
import matplotlib.pyplot as plt
import numpy as np

def setup():
    global ax, fig, x
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.arange(-10., 10., 0.2)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)
    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    





def onclick(event):
    print("click")
    print(event.xdata)
    print(event.ydata)

    plt.ion()

    global ax
    ax.plot(event.xdata, event.ydata, 'ro')
    if(len(points)<5):
        points.append(event.xdata)
        points.append(event.ydata)


    if(len(points)%2==0 and len(points)!=0):
        try:
            global x
            slope = (points[3] - points[1]) / (points[2] - points[0])

            temp = slope * points[0]

            b = points[1] - (slope * points[0])
            xd = np.linspace(-10,10,100)

            te = slope * x + b
            plt.plot(xd,te, '-r')

            print("googgo")
            points.clear()
        except:
            pass

    plt.ioff()

def startGui():
    global cid, plt
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.plot()
    plt.show()

points = []
fig = 0;
ax = 0;
x = 0;
setup()
startGui()