import matplotlib.pyplot as plt
import numpy as np
from classes import *
def draw_graf(obj):
    R=obj.real_r
    if obj.type == 'sputnic':
        obj = obj.main
    if obj.center!=1:
        gr = plt.plot(obj.ox, obj.oy)
        plt.xlabel('time')
        plt.ylabel('distant')
        plt.legend(['relative min distant '+str(min(obj.oy)/R)])
        plt.show()