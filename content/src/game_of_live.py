#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  game_of_live.py
# Datum:   19.02.2013 22:27
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
# Licence: GNU/GPL
# Úloha:   hra života
#          http://cs.wikipedia.org/wiki/Hra_živo ta
###################################################

import random
import pylab as lab
import matplotlib.animation as animation

# ########################## rozměry #####################################
w = 2**7
h = w
##########################################################################


def onclick(event):
    global data
    new = [[0 for i in range(w)] for j in range(h)]
    for m in range(h):
        for n in range(w):
            i = m if m != h-1 else -1
            j = n if n != w-1 else -1
            suma = data[i+1][j] + data[i-1][j] + \
                data[i][j+1] + data[i][j-1] + \
                data[i+1][j+1]+data[i-1][j-1] + \
                data[i+1][j-1]+data[i-1][j+1]
# ##################### ############ 23/3 Game of Live
            if data[i][j] == 1:
                if suma < 2:
                    new[i][j] = 0
                elif suma > 3:
                    new[i][j] = 0
                else:
                    new[i][j] = 1
            else:
                if suma == 3:
                    new[i][j] = 1
                else:
                    new[i][j] = 0
# ##################### ########### 125/36 Hodně oscilátorů a lodí
#            if data[i][j] == 1:
#                if suma == 1 or suma == 2 or suma == 5:
#                    new[i][j] = 1
#                else:
#                    new[i][j] = 0
#            else:
#                if suma == 3 or suma == 6:
#                    new[i][j] = 1
#                else:
#                    new[i][j] = 0
#  ##################### ########### 34/34
#            if data[i][j] == 1:
#                if suma == 3 or suma == 4:  # or suma == 5 or suma == 8:
#                    new[i][j] = 1
#                else:
#                    new[i][j] = 0
#            else:
#                if suma == 3 or suma == 4:  # or suma == 7:
#                    new[i][j] = 1
#                else:
#                    new[i][j] = 0
# ##################### ########### 245/368
#            if data[i][j] == 1:
#                if suma == 2 or suma == 4 or suma == 5:
#                    new[i][j] = 1
#                else:
#                    new[i][j] = 0
#            else:
#                if suma == 3 or suma == 6 or suma == 8:
#                    new[i][j] = 1
#                else:
#                    new[i][j] = 0
###################################################
    data = new
    grid.set_array(data)
    lab.draw()
#    print event.button
######################


data = [[random.randint(0, 7) for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        data[i][j] = data[i][j] if data[i][j] == 1 else 0

fig = lab.figure()
sub = lab.subplot(111)
sub.axes.get_xaxis().set_visible(False)
sub.axes.get_yaxis().set_visible(False)

grid = lab.imshow(data, interpolation='none', cmap='binary')
lab.grid()

ani = animation.FuncAnimation(fig, onclick, interval=300)
lab.show()

# cid = fig.canvas.mpl_connect('button_press_event', onclick)
# cid = fig.canvas.mpl_connect('key_press_event', on_key)
# def on_key(event):
#   print('you pressed', event.key, event.xdata, event.ydata)
