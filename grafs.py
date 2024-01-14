import matplotlib.pyplot as plt
import numpy as np
from classes import *


def draw_graf(obj, points):
    R = obj.real_r
    if obj.type == 'sputnic':
        obj = obj.main
    if obj.center != 1:
        gr = plt.plot(obj.ox, obj.oy)
        for i in points:
            plt.plot([i for q in range(len(obj.oy)+1)], obj.oy+[min(obj.oy)-0.05*(max(obj.oy)-min(obj.oy))], color='g')
        plt.xlabel('time, с')
        plt.ylabel('distant, м')
        #plt.legend(['relative min distant '+str(round(min(obj.oy)/R,2))+'\n'+'min distant '+str(round(min(obj.oy)/10**9,3)) +'*10^9 м'])
        plt.legend(['min distant '+str(round(min(obj.oy)/10**9,3)) +'*10^9 м'])
        plt.show()
    