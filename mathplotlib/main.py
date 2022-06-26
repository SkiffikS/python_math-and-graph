# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from rich import print # бібліотка для виводу різнокольорового тесту в консоль

# інсталяція бібліотек:
# pip install -r requirements.txt

print("[bold red]Особливості бібліотеки matplotlib: [/bold red]")


plt.style.use('dark_background') # тема заднього фону
print("[italic blue]1. Mathlib можна кастимізувати на любий смак\n(вибрати колір лінійЮ графіків та фону)[/italic blue]")


fig, ax = plt.subplots()

L = 6
x = np.linspace(0, L)
ncolors = len(plt.rcParams['axes.prop_cycle']) # список із кольорів
shift = np.linspace(0, L, ncolors, endpoint=False) # список із ліній
for s in shift:
    ax.plot(x, np.sin(x + s), 'o-') # Через цикл додаємо їх на графік
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title("'dark_background' style sheet")

plt.savefig(r"reports/images/graph_1.png") # Зберігаємо за шляхом
plt.savefig(r"reports/PDF/graph_1.pdf")

plt.show() # дамонструємо

print("[italic blue]2. Mathlib співпрацює із Numpy[/italic blue]")
print("[italic blue]3. У mathlib можна зберігати результат у багатьох видах\n(png, jpeg, PDF ...)[/italic blue]")

def gradient_image(ax, extent, direction=0.03, cmap_range=(0, 5), **kwargs):
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)]) # функції синуса і косинуса у списку для візулізації
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                  [v @ [0, 0], v @ [0, 1]]]) # основне рівняння
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(X, extent=extent, interpolation='bicubic', vmin=0, vmax=1, **kwargs) # параметри візуалізації
    return im

def grabargraph(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y): # збираємо значення у кортежі
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top), cmap='inferno', cmap_range=(0, 0.8)) # демонструємо

xmin, xmax = xlim = 0, 24
ymin, ymax = ylim = 0, 1

fig, ax = plt.subplots()
ax.set(xlim=xlim, ylim=ylim)

N = 24
x = np.arange(N) + 0.15
y = np.random.rand(N) # список із N рандомниї числе
grabargraph(ax, x, y, width=0.7)
ax.set_aspect('auto')
ax.set_title('Gradient Bar Graph')

plt.savefig(r"reports/images/graph_2.png")
plt.savefig(r"reports/PDF/graph_2.pdf")

plt.show()

print("[italic blue]3. У mathplotlib можна робити стовпцеві діаграми[/italic blue]")
print("[italic blue]Також у mathplotlib можна робити градієнт[/italic blue]")


labels = 'Python', 'C++', 'Ruby', 'Java' # назви відділень
sizes = [215, 130, 245, 210] # їх значення
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'] # кольори
explode = (0.1, 0, 0, 0)  # відриваємо першу частину від основного тіла

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140) 

plt.axis('equal')

plt.savefig(r"reports/images/graph_3.png")
plt.savefig(r"reports/PDF/graph_3.pdf")

plt.show()

print("[italic blue]4. У mathplotlib можна робити кругову статистику із процентним співвідношенням[/italic blue]")

def simplePloter(): # кругова діаграма

    N = 100
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint = False) # значення
    radii = 10*np.random.rand(N) # радіуси
    width = np.pi / 4 * np.random.rand(N) # висота
    ax = plt.subplot(111, projection = 'polar')
    bars = ax.bar(theta, radii, width = width, bottom = 0.0)
    for r, bar in zip(radii, bars): # проходимось по значенням та радіусам
        bar.set_facecolor(plt.cm.jet(r / 10.)) # збільшуємо кадіус із кожним циклом
        bar.set_alpha(0.8) # прозорість
    plt.savefig(r"reports/images/graph_4.png")
    plt.savefig(r"reports/PDF/graph_4.pdf")
    plt.show()

simplePloter()

print("[italic blue]5. Mathplotlib також дозволяє створювати кругові діаграми які переважно використовують для візуалізації тривалості режимів вітрової активності[/italic blue]")