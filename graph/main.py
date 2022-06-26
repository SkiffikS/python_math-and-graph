# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
# Імпортуємо модулі

plt.style.use('dark_background')
# Задаємо темний фон у графіках

TEXT = """
What is Education
The first thing that strikes in our minds when we think about education is gaining knowledge 
Education is a tool which provides people with knowledge skill technique information 
enables them to know their rights and duties toward their family society as well as the nation 
It expands vision and outlook to see the world It develops the capabilities to fight against injustice 
violence corruption and many other bad elements in the society
Education gives us knowledge of the world around us It develops in us a perspective of 
looking at life It is the most important element in the evolution of the nation 
Without education one will not explore new ideas It means one will not able to 
develop the world because without ideas there is no creativity and without creativity 
there is no development of the nation
"""
# Даний текст вставляємо в рядок зверху

def stringToList(string):
    # Функція переводу тексту у список із слів
    listRes = list(string.split(" "))
    return listRes


def wordsTop(text = TEXT): # Задаємо параметр текст по стандарту

    MyList = stringToList(text) # Получаємо список із слів

    res = {} # Створюємо словник у який будемо записувати слова та їх кількість у тексті
    for i in MyList: # проходимось по кожному слову
        res[i] = MyList.count(i) # Записуємо у словник

    words = []
    numbers = []

    for k, v in res.items(): # Проходимось по словнику

        words.append(k) # Получаємо слова
        numbers.append(v) # Получаємо їх кількість

    sorted_words = []
    sorted_numbers = []

    for i in range(len(numbers)): # сортуємо по кількості

        if len(sorted_numbers) >= 30: # обмеження довжини
            break
        index_min = min(range(len(numbers)), key = numbers.__getitem__) # Получаємо індекс мінімального елемента
        if numbers[index_min] == 1: # перевіряємо чи слово не зустрічається лише 1 раз
            del numbers[index_min] # Якщо так
            del words[index_min] # видаляємо слово та його кількість
        else: # У іншому випадку 
            sorted_words.append(words[index_min]) # Додаємо до списка слово по індексу
            sorted_numbers.append(numbers[index_min]) # Додаємо його кількість по індексу
            del numbers[index_min] # Видалаємо із списку
            del words[index_min] # щоб ці слова і індекси не попадались на наступних ітераціях
 
    fig, ax = plt.subplots() # створюємо фігури
    bar = ax.barh(sorted_words, sorted_numbers) # Додаємо їх у стовбцеву діаграмму
    grad = np.atleast_2d(np.linspace(0, 1, 256)) # Получаємо кольори для градієнта
    ax = bar[0].axes # Заповнюємо фігуру з першого елемента
    lim = ax.get_xlim() + ax.get_ylim()
    for bar in bar:
        bar.set_zorder(1)
        bar.set_facecolor("none")
        x, y = bar.get_xy()
        w, h = bar.get_width(), bar.get_height()
        ax.imshow(grad, extent = [x, x + w, y, y + h], aspect = "auto", zorder = 0)
    ax.axis(lim)
    plt.title('Скільки раз слова зустрічаються у тексті')
    plt.xlabel('Їх кількість')
    plt.savefig("reports/words_top.png")
    plt.savefig("reports/words_top.pdf")
    plt.show()


def middleLenght(text = TEXT):

    MyList = stringToList(text)
    Lenght_list = [] # Список із довжиною слів

    for i in MyList:

        Lenght_list.append(len(i)) # Заповнюємо список

    res = {} # словник із кількістю одинакових довжин
    for i in Lenght_list: # проходимось по списку довжин слів
        res[i] = Lenght_list.count(i) # заповнюємо словник 

    lenght = []
    numbers = []

    for k, v in res.items():

        lenght.append(k) # Получаємо дані із словника у списки
        numbers.append(v)

    sorted_lenght = []
    sorted_numbers = []

    for i in range(len(numbers)):

        index_min = min(range(len(numbers)), key=numbers.__getitem__) # Сортуємо списки по мінімальному індексу
        sorted_lenght.append(lenght[index_min])
        sorted_numbers.append(numbers[index_min])
        del numbers[index_min]
        del lenght[index_min]

    fig, ax = plt.subplots() #
    bar = ax.bar(sorted_lenght, sorted_numbers)

    grad = np.atleast_2d(np.linspace(0, 1, 256)).T # Получаємо те перевертаємо градієнт
    ax = bar[0].axes
    lim = ax.get_xlim()+ax.get_ylim()
    for bar in bar:
        bar.set_zorder(1)
        bar.set_facecolor("none")
        x, y = bar.get_xy()
        w, h = bar.get_width(), bar.get_height()
        ax.imshow(grad, extent=[x, x+w, y, y+h], aspect="auto", zorder=0)
    ax.axis(lim)
    plt.title('середня довжина слів')
    plt.ylabel('Кількість слів із даною довжиною')
    plt.xlabel('Довжина слів')
    plt.savefig("reports/words_lenght.png")
    plt.savefig("reports/words_lenght.pdf")
    plt.show()


if __name__ == "__main__": # Початок виконання программи

    middleLenght() # Викликаємо функції
    wordsTop()
