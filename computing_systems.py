import random
import numpy as np


class Event:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def show(self):
        print(self.name, '--', self.time)


f = int(input("Выберите функцию: \n 1. Ввести с клавиатуры \n 2. Запустить стандартные значения \n"))

if f == 1:
    print('Введите последовательно следующую информацию:')
    print()
    tasks = int(input('Кол-во заявок: '))
    # стандарт 200

    weight_1, weight_2, weight_3 = map(float, input('Веса распределения на три ЭВМ, через пробел: ').split())
    # стандарт 0.4 0.3 0.3

    weight_evm_1_to_2, weight_evm_1_to_3 = map(float,
                                               input(
                                                   'Веса распределения из ЭВМ_1 в ЭВМ_2 и ЭВМ_3, через пробел: ').split())
    # стандарт 0.3 0.7

    a1, b1 = map(int, input('Интервалы для ЭВМ_1, через пробел: ').split())
    # стандарт 3 5

    a2, b2 = map(int, input('Интервалы для ЭВМ_2, через пробел: ').split())
    # стандарт 2 4

    a3, b3 = map(int, input('Интервалы для ЭВМ_3, через пробел: ').split())
    # стандарт 3 7
elif f == 2:
    # количество заданий
    tasks = 200

    # вероятность поступления заданий
    weight_1 = 0.4
    weight_2 = 0.3
    weight_3 = 0.3

    # вероятность перехода заданий на другую эвм
    weight_evm_1_to_2 = 0.3
    weight_evm_1_to_3 = 0.7

    # интервалы времени
    a1 = 4
    a2 = 3
    a3 = 5

    b1 = 1
    b2 = 1
    b3 = 2
else:
    print("Неверная цифра!")

events = []
now_time = 0

count_kanals=3
# глобальные переменные для ЭВМ 1
evm_1_total_tasks = 0
evm_1_total_time = 0
evm_1_last = 0
evm_1_relax = 0
evm_1_total_relax = 0
evm_1_total_queue = 0
evm_1_total = 0

# глобальные переменные для ЭВМ 2
evm_2_total_tasks = 0
evm_2_total_time = 0
evm_2_last = 0
evm_2_relax = 0
evm_2_total_relax = 0
evm_2_total = 0
evm_2_total_queue = 0
flag_2 = 0

# глобальные переменные для ЭВМ 3
evm_3_total_tasks = 0
evm_3_total_time = 0
evm_3_last = 0
evm_3_relax = 0
evm_3_total_relax = 0
evm_3_total = 0
evm_3_total_queue = 0
flag_3 = 0


def evm_1(task_number):
    global now_time, evm_1_relax, evm_1_last, evm_1_total_time, evm_1_total_relax, evm_1_total_tasks, evm_1_total_queue

    # кол-во заявок
    evm_1_total_tasks += 1

    # время простоя
    evm_1_relax = now_time - evm_1_last
    if evm_1_relax < 0:
        evm_1_relax = 0

    # если нужно время ожидания между заявками
    # то выводим каждый раз evm_1_relax

    # общее время простоя
    evm_1_total_relax += evm_1_relax

    # поступление заявки
    task_start = Event('ЭВМ 1 поступила заявка {}'.format(task_number), now_time)
    start_queue = now_time

    # время выполнения заявки
    evm_1_work = np.random.uniform(a1, b1)
    global evm_1_w
    evm_1_w = evm_1_work
    # evm_1_work = 10

    # время конца работы
    # если заявка есть
    if evm_1_last > now_time:
        evm_1_last = evm_1_last + evm_1_work
    # если заявки нет
    else:
        evm_1_last = now_time + evm_1_work

    # выполнение заявки
    task_end = Event('ЭВМ 1 выполнена заявка {}'.format(task_number), evm_1_last)
    end_queue = evm_1_last
    evm_1_total_queue += end_queue - start_queue

    # общее время работы = время всего простоя + время всей работы
    evm_1_total_time = evm_1_total_time + evm_1_relax + evm_1_work

    # заносим события в список
    events.append(task_start)
    events.append(task_end)

    # передаем задачу другой ЭВМ
    next_evm_number = random.choices((2, 3), weights=[weight_evm_1_to_2, weight_evm_1_to_3])

    # ЭВМ 2
    if next_evm_number == [2]:
        evm_2(i, 1, evm_1_last)

    # ЭВМ 3
    elif next_evm_number == [3]:
        evm_3(i, 1, evm_1_last)


def evm_2(task_number, enemy_task, enemy_time):
    global now_time, evm_2_relax, evm_2_last, evm_2_total_time, evm_2_total_relax, evm_2_total_tasks, evm_2_total_queue

    # кол-во заявок
    evm_2_total_tasks += 1

    # поступила задача от ЭВМ 1
    if enemy_task == 1:
        now_time = enemy_time

    # время простоя
    evm_2_relax = now_time - evm_2_last
    if evm_2_relax < 0:
        evm_2_relax = 0

    # если нужно время ожидания между заявками
    # то выводим каждый раз evm_2_relax

    # общее время простоя
    evm_2_total_relax += evm_2_relax

    # поступление заявки
    if enemy_task == 0:
        task_start = Event('ЭВМ 2 поступила заявка {}'.format(task_number), now_time)
    else:
        task_start = Event('ЭВМ 2 передана заявка {} от ЭВМ 1'.format(task_number), now_time)
    start_queue = now_time

    # время выполнения заявки
    evm_2_work = np.random.uniform(a2, b2)
    global evm_2_w
    evm_2_w = evm_2_work
    # evm_2_work = 10

    # время конца работы
    # если заявка есть
    if evm_2_last > now_time:
        evm_2_last = evm_2_last + evm_2_work
    # если заявки нет
    else:
        evm_2_last = now_time + evm_2_work

    # выполнение заявки
    if enemy_task == 0:
        task_end = Event('ЭВМ 2 выполнена заявка {}'.format(task_number), evm_2_last)
    else:
        task_end = Event('ЭВМ 2 выполнена переданная заявка {} от ЭВМ 1'.format(task_number), evm_2_last)
    end_queue = evm_2_last
    evm_2_total_queue += end_queue - start_queue

    # общее время работы = время всего простоя + время всей работы
    evm_2_total_time = evm_2_total_time + evm_2_relax + evm_2_work

    # заносим события в список
    events.append(task_start)
    events.append(task_end)


def evm_3(task_number, enemy_task, enemy_time):
    global now_time, evm_3_relax, evm_3_last, evm_3_total_time, evm_3_total_relax, evm_3_total_tasks, evm_3_total_queue

    # кол-во заявок
    evm_3_total_tasks += 1

    # поступила задача от ЭВМ 1
    if enemy_task == 1:
        now_time = enemy_time

    # время простоя
    evm_3_relax = now_time - evm_3_last
    if evm_3_relax < 0:
        evm_3_relax = 0

    # если нужно время ожидания между заявками
    # то выводим каждый раз evm_3_relax

    # общее время простоя
    evm_3_total_relax += evm_3_relax

    # поступление заявки
    if enemy_task == 0:
        task_start = Event('ЭВМ 3 поступила заявка {}'.format(task_number), now_time)
    else:
        task_start = Event('ЭВМ 3 передана заявка {} от ЭВМ 1'.format(task_number), now_time)
    start_queue = now_time

    # время выполнения заявки
    evm_3_work = np.random.uniform(a3, b3)
    global evm_3_w
    evm_3_w = evm_3_work
    # evm_3_work = 10

    # время конца работы
    # если заявка есть
    if evm_3_last > now_time:
        evm_3_last = evm_3_last + evm_3_work
    # если заявки нет
    else:
        evm_3_last = now_time + evm_3_work

    # выполнение заявки
    if enemy_task == 0:
        task_end = Event('ЭВМ 3 выполнена заявка {}'.format(task_number), evm_3_last)
    else:
        task_end = Event('ЭВМ 3 выполнена переданная заявка {} от ЭВМ 1'.format(task_number), evm_3_last)
    end_queue = evm_3_last
    evm_3_total_queue += end_queue - start_queue

    # общее время работы = время всего простоя + время всей работы
    evm_3_total_time = evm_3_total_time + evm_3_relax + evm_3_work

    # заносим события в список
    events.append(task_start)
    events.append(task_end)


for i in range(1, tasks + 1):
    task_interval = np.random.uniform(2, 4)
    global interval
    interval = task_interval
    evm_number = random.choices((1, 2, 3), weights=[weight_1, weight_2, weight_3])
    # добавляем время выдачи задачи
    now_time += task_interval

    # ЭВМ 1
    if evm_number == [1]:
        evm_1(i)

    # ЭВМ 2
    elif evm_number == [2]:
        evm_2(i, 0, 'str')

    # ЭВМ 3
    elif evm_number == [3]:
        evm_3(i, 0, 'str')

events_sorted = sorted(events, key=lambda x: x.time, reverse=True)
for i in events_sorted:
    i.show()



l1=weight_1/a1
l2=weight_2/a2
l3=weight_3/a3
# суммарная интенсивность потока заявок для всех эвм
l=l1+l2+l3

# интенсивности обслуживания на каждой ЭВМ
fi1=1/a1
fi2=1/a2
fi3=1/a3

# средние загрузки каждой из ЭВМ
ro=l/(fi1+fi2+fi3)
ro1=l1/fi1
ro2=l2/fi2
ro3=l3/fi3


# среднее число каналов в обслуживании
Cs=l*(weight_1*a1+weight_2*a2+weight_3*a3)

# среднее время, которое заявка проводит в очереди
Wq=(ro1**2+ro2**2+ro3**2)/(2*(1-ro1)*l)
# среднее число заявок в очереди
Lq=l*Wq

lis=l*Cs
# среднее число заявок в системе
L=Lq+lis
# среднее время пребывания заявки в системе
# W=L/l

W2=round( (evm_1_total_relax + evm_2_total_relax + evm_3_total_relax) / (
        evm_1_total_tasks + evm_2_total_tasks + evm_3_total_tasks),2)

evm1_zan=round(evm_1_total_time - evm_1_total_relax,1)
print('')
print('Статистика ЭВМ 1:')
print('Кол-во заявок:', evm_1_total_tasks)
print('Общее время работы:', round(evm_1_total_time,2),'мин')
print('Время занятости ЭВМ:', round(evm1_zan,1),'мин')
print('Время простоя ЭВМ:', round(evm_1_total_relax,1),'мин')
print('Коэффициент занятости:', round(evm1_zan / evm_1_total_time,2)*100,'%')
print('Коэффициент простоя:', round(evm_1_total_relax/ evm_1_total_time,2)*100,'%')
# мы больше ждем заявок, чем они ждут в очереди, это можно увидеть во времени простоя
queue_1 = float(abs(evm_1_total_time - evm_1_total_relax - evm_1_total_queue) / evm_1_total_tasks)
print('Среднее время ожидания в очереди', round(queue_1,1),'мин')

evm2_zan=evm_2_total_time-evm_2_total_relax
print('')
print('Статистика ЭВМ 2:')
print('Кол-во заявок:', evm_2_total_tasks)
print('Общее время работы:', round(evm_2_total_time,1),'мин')
print('Время занятости ЭВМ:',round(evm2_zan),1,'мин')
print('Время простоя ЭВМ:', round(evm_2_total_relax,1),'мин')
print('Коэффициент занятости:', round(evm2_zan / evm_2_total_time,2)*100,'%')
print('Коэффициент простоя:', round(evm_2_total_relax/ evm_2_total_time,2)*100,'%')
# мы больше ждем заявок, чем они ждут в очереди, это можно увидеть во времени простоя
queue_2 = float(abs(evm_2_total_time - evm_2_total_relax - evm_2_total_queue) / evm_2_total_tasks)
print('Среднее время ожидания в очереди', round(queue_2,2),'мин')

evm3_zan=evm_3_total_time-evm_3_total_relax
print('')
print('Статистика ЭВМ 3:')
print('Кол-во заявок:', evm_3_total_tasks)
print('Общее время работы:', round(evm_3_total_time,1),'мин')
print('Время занятости ЭВМ:',round(evm3_zan),1,'мин')
print('Время простоя ЭВМ:', round(evm_3_total_relax,1),'мин')
print('Коэффициент занятости:', round(evm3_zan / evm_3_total_time,2)*100,'%')
print('Коэффициент простоя:', round(evm_3_total_relax/ evm_3_total_time,2)*100,'%')
#
queue_3 = float(abs(evm_3_total_time - evm_3_total_relax - evm_3_total_queue) / evm_3_total_tasks)
print('Среднее время ожидания в очереди', round(queue_3,1))


print('')
print("Общая статистика работы системы:")
print('Время работы системы:', round(events_sorted[0].time - events_sorted[len(events_sorted) - 1].time,2),'мин.')
print('Среднее время ожидания в очереди', round (((queue_1 + queue_2 + queue_3) / 3.0),2),'мин.')
print('Среднее число каналов в обслуживании=', Cs)
print('Среднее число заявок в очереди', round(Lq))
print('Среднее число заявок в системе', round(L))
print('Среднее время пребывания заявки в системе:',W2,'мин.')


# РЕКОМЕНДАЦИИ ЗАВИСЯТ ОТ ВХОДНЫХ ДАННЫХ
# направить больше заявок на 2 и 3 машины, т.к. первая работает, но все равно отдает на 2 и 3, в идеале свести к нулю))
# при этом распределение из 1 машины во 2 и 3 сделать даже [0.8:0.2], т.к. ЭВМ 2 работает быстрее ЭВМ 3
# 'улучшить' / 'заменить на новые', у которых время выполнения заявок меньше
