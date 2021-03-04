#https://matplotlib.org/3.3.3/users/event_handling.html
import matplotlib.pyplot as plt
import numpy as np
from somenamepy.graph import graph

def setup(g):
    global ax, fig
    fig = plt.figure()
    ax = fig.add_subplot(111)
    g._x = np.arange(-10., 10., 0.2)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

def onclick(event):

    plt.ion()
    global ax, g
    if(len(g._points)<5):
        ax.plot(event.xdata, event.ydata, 'ro')
        appendPointsToArray([event.xdata, event.ydata])
    
    if(len(g._points)==4 and len(g._points)!=0):
        try:
            g._slope = (g._points[3] - g._points[1]) / (g._points[2] - g._points[0])
            g._b = g._points[1] - (g._slope * g._points[0])
            calcFunc(g)
            g._lines = plt.plot(g._x,g._func, '-r')

            #points.clear()
        except:
            pass

    plt.ioff()

def onrelease(event):
    global ax, g
    if(g._lines != 0):
        x1,x2 = ax.get_xlim()
        g._x = np.arange(x1,x2,0.2)
        calcFunc(g)
        removeGraphOutOfView(g)
        reDrawGraph(g)

def removeGraphOutOfView(g):
    l = g._lines.pop(0)
    l.remove()
    del l

def reDrawGraph(g):
    g._lines = plt.plot(g._x,g._func, '-r')

def calcFunc(g):
    g._func = g._slope * g._x + g._b

def appendPointsToArray(data):
    for entry in data:
        g._points.append(entry)

def start():
    global cid, plt
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    cid = fig.canvas.mpl_connect('button_release_event', onrelease)
    plt.plot()
    plt.show()


fig = 0
ax = 0
g = graph([],0,0,0,0,0,0)
setup(g)
start()
#for every new graph instatiate new graph object. 
#save that object in some datastructure with a unique id.
#write someting that keeps this data structre sorted and withouts empty positions