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
        plt.xlabel('time')
        plt.ylabel('distant')
        plt.legend(['relative min distant '+str(min(obj.oy)/R)])
        plt.show()
    