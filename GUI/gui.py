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
    #print(event.xdata)
    #print(event.ydata)

    plt.ion()

    global ax
    
    if(len(points)<5):
        ax.plot(event.xdata, event.ydata, 'ro')
        points.append(event.xdata)
        points.append(event.ydata)


    if(len(points)==4 and len(points)!=0):
        try:
            global x, te,b,slope
            slope = (points[3] - points[1]) / (points[2] - points[0])

            temp = slope * points[0]

            b = points[1] - (slope * points[0])
            xd = np.linspace(-10,10,100)

            te = slope * x + b
            plt.plot(x,te, '-r')

            print(te)
            #points.clear()
        except:
            pass

    plt.ioff()

def onrelease(event):
    global ax, x, slope,b
    x1,x2 = ax.get_xlim()
    print(ax.get_xlim())
    print(ax.get_ylim())
    x = np.arange(x1,x2,0.2)
    func = slope * x + b
    print(te)
    plt.plot(x,func, '-r')

def start():
    global cid, plt
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    cid = fig.canvas.mpl_connect('button_release_event', onrelease)
    plt.plot()
    plt.show()

points = []
fig = 0
ax = 0
x = 0
te = 0
slope = 0
b = 0
setup()
start()
#for every new graph instatiate new graph object. 
#save that object in some datastructure with a unique id.
#write someting that keeps this data structre sorted and withouts empty positions