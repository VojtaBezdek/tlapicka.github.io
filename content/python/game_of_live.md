Title: Hra života -- Game of live
Date: 2015-06-08 14:41
Category: Blog
Tags: python
Author: Marek Nožka

[Hra života]: http://cs.wikipedia.org/wiki/Hra_života
[matplotlib]: http://matplotlib.org/

[Hra života][] je dvoustavový, dvourozměrný celulární automat, který svým
chováním připomíná vývoj společenství živých organismů. Odehrává se na matici
buněk, jejíž stav předurčuje podobu hry v následujícím kroku.

Už moc nevím, kde jsem se k této hře nebo algoritmu dostal, ale docela se mi
tato myšlenka zalíbila. Pro implementaci stačí dvourozměrná matice čísel 0 a 1,
které představují mrtvé a živé buňky. O tom, jak bude matice vypadat v
následujícím kroku se rozhodne podle těchto pravidel:

1. Každá živá buňka s méně než dvěma živými sousedy zemře.
2. Každá živá buňka se dvěma nebo třemi živými sousedy zůstává žít.
3. Každá živá buňka s více než třemi živými sousedy zemře.
4. Každá mrtvá buňka s právě třemi živými sousedy oživne.

Pro zobrazení a animaci jsem použil modul [matplotlib][].

![001011110010001010101110]({filename}/img/gameoflive.png)

[game_of_live.py]({filename}/src/game_of_live.py)

    :::python
    import random
    import pylab as lab
    import matplotlib.animation as animation

    w = 2**7
    h = w

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
        data = new
        grid.set_array(data)
        lab.draw()


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

Pravidla lze samozřejmě 
[upravovat](http://cs.wikipedia.org/wiki/Hra_života#Pravidla_celul.C3.A1rn.C3.ADch_automat.C5.AF_zalo.C5.BEen.C3.BDch_na_H.C5.99e_.C5.BEivota)
-- lze tak dosáhnout poměrně zajímavých výsledků...
